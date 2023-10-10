def dfs(graph,node, visited):
    visited[node]= True
    for v in graph[node]:
        if not visited[v]:
            dfs(graph,node,visited)

from collections import deque
def bfs(graph,node,visited):
    q = deque([node])
    visited[node]=True
    while q:
        v=q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=True

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in (i+1,len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i],array[j] = array[j],array[i]

def selection_sort(array):
    for i in(1,range(len(array))):
        for j in (i,0,-1):
            if array[j]<array[j-1]:
                array[j],array[j-1]=array[j-1],array[j]
            else:
                break

def quick_sort(array,start,end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left<=end and array[pivot] >= array[left]:
            left += 1
        while right>start and array[pivot]<=array[right]:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
        else:
            array[pivot], array[right] = array[right], array[pivot]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

def sort(array,count):
    for i in array:
        count[i]+=1
    for j in range(len(count)):
        for k in range(count[j]):
            print(j)

def sequential_sort(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
        
def binary_search(array,target,start,end):
    if start >end:
        return 
    mid = (start+end)//2
    if array[mid] < target:
        binary_search(array,target,mid+1,end)
    elif array[mid] > target:
        binary_search(array,target,start,mid-1)
    else:
        return mid

def binary_search_repeat(array,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            return mid
    return 


import sys
input = sys.stdin.readline

d = [0]*100
def dynamic_recursive(x):
    if x==1 or x==2:
        return 1
    elif d[x] != 0:
        return d[x]
    else:
        d[x]=d[x-1]+d[x-2]
        return d[x]
print(dynamic_recursive(99))
def dynamic_repeat(n):
    if n==1 or n==2:
        d[n]=1
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]
dynamic_repeat(99)
print(d[99])

import heapq
import sys
input = sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
graph=[[]for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a]=(b,c)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop()
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

def binary_search(data,list):
    start=0
    end=len(list)-1
    result=-1
    while start<=end:
        mid = (start+end)//2
        if data <=list[mid]:
            end=mid-1
        else:
            start=mid+1
            result=mid
    return result

def dfs(graph,node,visited):
    visited[node]=True
    for v in graph[node]:
        if not visited[v]:
            dfs(graph,v,visited)

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

def quick_sort(array,start,end):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end
    while left<=right:
        while array[pivot] >=array[left]:
            left+=1
        while array[pivot] <=array[right]:
            right-=1
        if left > right:
            array[right],array[pivot]=array[pivot],array[right]
        else:
            array[left],array[right]=array[right],array[left]



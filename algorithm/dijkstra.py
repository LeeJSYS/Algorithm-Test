import sys
input = sys.stdin.readline
INF = int(1e9)

# n,m : 노드, 간선 수
n,m=map(int,input().split())
start = int(input())

graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for _ in range(n+1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))#a->b : c

def smallest_node():
    min_value = INF
    min_index = 0
    for i in range(1,n+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            min_index = i
    return min_index

def dijkstra(start):
    visited[start]=True
    distance[start]=0
    for i in graph[start]:
        distance[i[0]]=i[1]
    for i in range(1,n-1):
        next_node = smallest_node()
        visited[next_node]=True
        for j in graph[next_node]:
            if distance[j[0]] > distance[next_node]+j[1]:
                distance[j[0]]=distance[next_node]+j[1]
    
        
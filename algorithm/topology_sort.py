from collections import deque

v, e = map(int,input().split())
indegree = [0]*(v+1)
graph = [[]for _ in range(v+1)]

for _ in range(e):
    a, b = map(int,input().split())
    graph[a]=b
    indegree[b]+=1

def topology_sort():
    start_index=0
    for i in range(1,v+1):
        if indegree[i]==0:
            start_index=i

    result=[]
    q = deque([start_index])
    while q:
        now=q.popleft()
        result.append(now)
        for node in graph[now]:
            indegree[node]-=1
            if indegree[node]==0:
                q.append(node)
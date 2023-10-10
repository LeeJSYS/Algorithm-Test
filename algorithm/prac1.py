def dfs(graph, node, visited):
    visited[node]=True
    for v in graph[node]:
        if not visited[v]:
            dfs(graph, v, visited)

from collections import deque
def bfs(graph, node, visited):
    q = deque([node])
    visited[node]=True
    while q:
        now=q.popleft()
        for v in graph[now]:
            if not visited[v]:
                q.append(v)
                visited[v]=True
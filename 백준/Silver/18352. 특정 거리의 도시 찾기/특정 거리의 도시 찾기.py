from collections import deque
import sys
input = sys.stdin.readline
# N: 도시 수, M: 도로 수, K: 거리, X: 출발도시
N,M,K,X=map(int,input().split())

INF = int(1e9)

graph=[[]for _ in range(N+1)]
distance=[INF for _ in range(N+1)]
visited=[False for _ in range(N+1)]

for _ in range(M):
    # a->b
    a,b = map(int,input().split())
    graph[a].append(b)


def bfs(start):
    visited[start]=True
    distance[start]=0
    q=deque([start])
    while q:
        now=q.popleft()
        for v in graph[now]:
            if not visited[v]:
                visited[v]=True
                distance[v]=distance[now]+1
                q.append(v)

bfs(X)
if K in distance:
    for i in range(1,len(distance)):
        if distance[i]==K:
            print(i)
else:
    print(-1)
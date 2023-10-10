import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m+1):
    # a-> b : cost가 c
    a,b,c = map(int,input().split())
    graph[a][b] = c

for i in range(1,n+1):
    graph[i][i] = 0

# Cab=min(Cab,Cak+Ckb)
for a in range(n+1):
    for b in range(n+1):
        for k in range(n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
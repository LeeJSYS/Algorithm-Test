import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# n,m : 노드, 간선 수
n,m = map(int,input().split())
start = int(input())

graph = [[] for i in range()]
distance = [INF]*(n+1)

for _ in range(n):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) # a->b의 비용이 c

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
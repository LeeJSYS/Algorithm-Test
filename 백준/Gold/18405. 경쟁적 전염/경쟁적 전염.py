import sys
input = lambda: sys.stdin.readline().rstrip()

n,virus_num = map(int, input().split())
graph = [[*map(int,input().split())] for _ in range(n)]
minute,row,col = map(int,input().split())

import heapq
virus = []
#바이러스위치저장
for i in range(n):#row
    for j in range(n):#col
        if graph[i][j]!=0:
            heapq.heappush(virus,(graph[i][j],(i,j)))

# def spread(r,c,num):
#     for move in ((-1,0),(0,-1),(1,0),(0,1)):
#         nr = r + move[0]
#         nc = c + move[1]
#         if nr < 0 or nr >= n or nc < 0 or nc >= n:
#             continue
#         if graph[nr][nc]!=0:
#             continue
#         graph[nr][nc] = num

for _ in range(minute):
    copy=virus[:]
    while copy:
        number, node = heapq.heappop(copy)
        # spread(node[0],node[1],number)
        for move in ((-1,0),(0,-1),(1,0),(0,1)):
            nr = node[0] + move[0]
            nc = node[1] + move[1]
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if graph[nr][nc]!=0:
                continue
            graph[nr][nc] = number
            heapq.heappush(virus,(number,(nr,nc)))
    if len(virus)==n*n:
        break

print(graph[row-1][col-1])
    

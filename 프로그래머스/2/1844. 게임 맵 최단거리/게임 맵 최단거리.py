from collections import deque
def solution(maps):
    n=len(maps)
    m=len(maps[0])
    visited=[[False for _ in range(m)] for _ in range(n)]
    result=[]
    
    def bfs(node,cnt):
        q = deque()
        q.append([node[0],node[1],cnt])
        visited[node[0]][node[1]]=True
        while q:
            x,y,cnts=q.popleft()
            dx=[-1,1,0,0]#상하좌우
            dy=[0,0,-1,1]
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if maps[nx][ny]==0:
                    continue
                if maps[nx][ny]==1 and not visited[nx][ny]:
                    maps[nx][ny]=-cnts
                    if nx==n-1 and ny==m-1:
                        result.append(cnts)
                    else:
                        visited[nx][ny]=True
                        q.append([nx,ny,cnts+1])
                    
    bfs((0,0),2)
    
    if len(result)==0:
        return -1
    else:
        return min(result)
    
#  GPT 답안
# from collections import deque

# def solution(maps):
#     n = len(maps)
#     m = len(maps[0])
#     visited = [[False for _ in range(m)] for _ in range(n)]
    
#     # 상하좌우 방향
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     def bfs():
#         q = deque()
#         q.append((0, 0))
#         visited[0][0] = True
        
#         while q:
#             x, y = q.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
                
#                 # 범위 밖이면 skip
#                 if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                     continue
#                 # 벽이거나 이미 방문한 곳이면 skip
#                 if maps[nx][ny] == 0 or visited[nx][ny]:
#                     continue
                
#                 # 현재 거리 + 1 누적
#                 maps[nx][ny] = maps[x][y] + 1
#                 visited[nx][ny] = True
#                 q.append((nx, ny))

#     bfs()
    
#     result = maps[n-1][m-1]
#     return result if result > 1 else -1

                
        
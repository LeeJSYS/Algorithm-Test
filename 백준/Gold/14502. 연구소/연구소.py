import sys
input = lambda: sys.stdin.readline().rstrip()

row,col = map(int, input().split())
graph = [[*map(int,input().split())] for _ in range(row)]
# graph = [list(map(int,input().split())) for _ in range(row)]

from itertools import combinations
point=[]
for i in range(row):
    for j in range(col):
        if graph[i][j]==0:
            point.append((i,j))
combi = list(combinations(point,3))

def dfs(x,y,copy):
    if x<0 or x>=row or y<0 or y>=col:
        return
    if copy[x][y]==2:
        for move in ((-1,0),(0,-1),(1,0),(0,1)):
            if x+move[0] < 0 or x+move[0]>=row or y+move[1] < 0 or y+move[1] >=col:
                continue
            if copy[x+move[0]][y+move[1]]==0:
                copy[x+move[0]][y+move[1]]=2
                dfs(x+move[0],y+move[1],copy)

result=0
for case in combi:
    copy=[]
    for i in range(row):
        copy.append(graph[i][:])
    for i in range(3):
        copy[case[i][0]][case[i][1]]=1
    for i in range(row):
        for j in range(col):
            dfs(i,j,copy)
    cnt=0
    for i in range(row):
        for j in range(col):
            if copy[i][j]==0:
                cnt+=1

    if result < cnt:
        result = cnt
print(result)



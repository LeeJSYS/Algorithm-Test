import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
timeTable = [list(map(int,input().split())) for _ in range(n)]

timeTable.sort(key= lambda x:(x[0], x[1]))

q=[]
start, end = timeTable[0]
heapq.heappush(q, end)

for i in range(1,n):
    start, end = timeTable[i]

    if q[0] <= start:
        heapq.heappop(q)
    heapq.heappush(q,end)

print(len(q))
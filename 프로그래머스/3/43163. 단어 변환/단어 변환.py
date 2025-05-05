# from collections import deque
# def solution(begin, target, words):
# #     n=len(words)
# #     l=len(words[0])
# #     visited=[False]*n
# #     result=[]
    
# #     def dfs(node,depth):
# #         now=node
# #         for i in range(n):
# #             if not visited[i]:
# #                 cnt=0
# #                 for j in range(l):
# #                     if words[i][j]!=node[j]:
# #                         cnt+=1
# #                     if cnt > 1:
# #                         break

# #                 if cnt==1 and not visited[i]:
# #                     now=words[i]
# #                     visited[i]=True

# #                 if now!=node:
# #                     if now == target:
# #                         result.append(depth)
# #                         visited[i]=False
# #                         return
# #                     if depth == len(words)-1:
# #                         return
# #                     dfs(now,depth+1)
# #                     visited[i]=False
# #         return
    
# #     dfs(begin,1)
# #     if len(result)>0:
# #         return min(result)
# #     else:
# #         return 0
#     if target not in words:
#         return 0
#     visited=set()
#     q=deque([(begin, 0)])
#     while q:
#         check, count = q.popleft()
#         if check == target:
#             return count
#         for word in words:
#             if word not in visited and can_change(check, word):
#                 visited.add(word)
#                 q.append((word, count+1))
#     return 0
    
# def can_change(start, target):
#     cnt=0
#     for i in range(len(start)):
#         if start[i]!=target[i]:
#             cnt+=1
#     if cnt == 1:
#         return True
#     else:
#         return False
    
from collections import deque
def solution(begin, target, words):
    visited=set()
    q=deque([(0,begin)])
    while q:
        cnt,node = q.popleft()
        if node == target:
            return cnt
        for word in words:
            if word not in visited and can_change(node, word):
                q.append((cnt+1,word))
                visited.add(word)
    return 0
    
def can_change(start, end):
    cnt=0
    for i in range(len(start)):
        if start[i]!=end[i]:
            cnt+=1
    if cnt==1:
        return True
    else:
        return False
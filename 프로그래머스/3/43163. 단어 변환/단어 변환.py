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
#             if word not in visited and can_change(word, target):
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
    if target not in words:
        return 0

    visited = set()
    queue = deque([(begin, 0)])  # (현재 단어, 현재까지의 단계 수)

    while queue:
        current, steps = queue.popleft()

        if current == target:
            return steps

        for word in words:
            if word not in visited and can_transform(current, word):
                visited.add(word)
                queue.append((word, steps + 1))

    return 0  # 변환 불가

def can_transform(word1, word2):
    return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1

    
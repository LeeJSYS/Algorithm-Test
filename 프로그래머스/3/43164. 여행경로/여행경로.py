from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    # 그래프 구성 (도착지를 알파벳 순으로 정렬하기 위해 역순 삽입)
    for a, b in tickets:
        graph[a].append(b)
    for key in graph:
        graph[key].sort(reverse=True)
    
    path = []

    def dfs(curr):
        while graph[curr]:
            next = graph[curr].pop()
            dfs(next)
        path.append(curr)  # 끝에서부터 추가 (뒤집을 것임)

    dfs("ICN")
    return path[::-1]
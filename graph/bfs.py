from collections import deque

# vertex = 시작 지점
# edge = 간선

# 인접 리스트
graph = {
    "A": ["B", "D", "E"],
    "B": ["A", "C", "D"],
    "C": ["B"],
    "D": ["A", "B"],
    "E": ["A"],
}


def bfs(graph, start_v):
    visited = [start_v]
    q = deque()
    q.append(start_v)

    while q:
        cur_v = q.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                q.append(v)
    return visited


# A,B,D,E,C
print(bfs(graph, "A"))

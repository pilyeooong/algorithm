from collections import defaultdict

v = [[1, 4], [3, 4], [3, 10]]


def solution(v):
    x_graph = defaultdict(int)
    y_graph = defaultdict(int)
    for x, y in v:
        x_graph[x] += 1
        y_graph[y] += 1

    for k, v in x_graph.items():
        if v == 1:
            x = k
    for k, v in y_graph.items():
        if v == 1:
            y = k
    return [[x, y]]


print(solution(v))

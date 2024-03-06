visited = []
graph = {
    "A": ["B", "D", "E"],
    "B": ["A", "C", "D"],
    "C": ["B"],
    "D": ["A", "B"],
    "E": ["A"],
}


def dfs(v):
    visited.append(v)
    for v in graph[v]:
        if v not in visited:
            dfs(v)
    return visited


# E A B C D
print(dfs("E"))

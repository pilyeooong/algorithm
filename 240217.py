from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
#     1
#   2   3
# 4   5
#

graph = {
    "A": ["B", "D", "E"],
    "B": ["A", "C", "D"],
    "C": ["B"],
    "D": ["A", "B"],
    "E": ["A"],
}


tree_dfs_visited = []
tree_bfs_visited = []


def tree_dfs(root):
    if root is None:
        return None
    tree_dfs_visited.append(root.value)
    tree_dfs(root.left)
    tree_dfs(root.right)

    return tree_dfs_visited


def tree_bfs(root):
    q = deque()
    q.append(root)
    while q:
        cur_node = q.popleft()
        tree_bfs_visited.append(cur_node.value)
        if cur_node.left is not None:
            q.append(cur_node.left)
        if cur_node.right is not None:
            q.append(cur_node.right)
    return tree_bfs_visited


print(tree_dfs(root))
print(tree_bfs(root))


graph_dfs_visited = []
graph_bfs_visited = []


def graph_dfs(v):
    graph_dfs_visited.append(v)
    for x in graph[v]:
        if x not in graph_dfs_visited:
            graph_dfs(x)
    return graph_dfs_visited


def graph_bfs(v):
    q = deque()
    q.append(v)
    graph_bfs_visited.append(v)
    while q:
        cur_v = q.popleft()
        for x in graph[cur_v]:
            if x not in graph_bfs_visited:
                graph_bfs_visited.append(x)
                q.append(x)
    return graph_bfs_visited


print(graph_dfs("E"))
print(graph_bfs("E"))

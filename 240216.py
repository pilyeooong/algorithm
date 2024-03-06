from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs(root):
    visited = []
    q = deque()
    q.append(root)

    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)

    return visited


dfs_visited = []


def dfs(root):
    if root is None:
        return None

    dfs(root.left)
    dfs_visited.append(root.value)
    dfs(root.right)

    return dfs_visited


def test():
    root = Node(3)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(4)

    print(bfs(root))
    print(dfs(root))


test()

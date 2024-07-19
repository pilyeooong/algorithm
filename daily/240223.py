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


def tree_bfs(root):
    q = deque()
    q.append(root)

    tree_bfs_visited = []

    while q:
        cur_node = q.popleft()
        tree_bfs_visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return tree_bfs_visited


tree_dfs_visited = []


def tree_dfs(root):
    if root is None:
        return None
    tree_dfs_visited.append(root.value)
    tree_dfs(root.left)
    tree_dfs(root.right)

    return tree_dfs_visited


print('bfs,dfs')
print(tree_bfs(root))
print(tree_dfs(root))

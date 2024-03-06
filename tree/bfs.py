from collections import deque


# level 단위로 하나씩 접근
# 트리에서 가로로 접근한다고 보면 됨
def bfs(root):
    visited = []

    if root is None:
        return 0

    q = deque()
    q.append(root)

    while q:
        current_node = q.popleft()
        visited.append(current_node.value)

        if current_node.left is not None:
            q.append(current_node.left)
        if current_node.right is not None:
            q.append(current_node.right)

    return visited


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
root.right.left = Node(6)
root.right.right = Node(7)

print(bfs(root))

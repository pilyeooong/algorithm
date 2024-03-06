from collections import deque


visited = []

# 전위 순회 - 부모 노드부터 방문하며 내려감
# 중위 순회 - 한쪽 자식노드부터 방문하고 나머지 자식노드 방문
# 후위 순회 - 자식 노드 부터 모두 방문하고 나서 부모 노드 방문


def dfs(root):
    if root is None:
        return
    dfs(root.left)
    dfs(root.right)
    visited.append(root.value)

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
print(dfs(root))
#     1
#   2   3
# 4   5
#

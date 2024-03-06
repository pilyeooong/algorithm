from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def first_solution(root):  # bfs
    if root is None:
        return 0

    q = deque()
    q.append([root, 1])
    max_depth = 1

    while q:
        current_node = q.popleft()
        max_depth = max(current_node[-1], max_depth)
        if current_node[0].left:
            q.append([current_node[0].left, current_node[-1] + 1])
        if current_node[0].right:
            q.append([current_node[0].right, current_node[-1] + 1])

    return max_depth


def max_depth_sol(root):  # dfs
    max_depth = 0
    if root is None:
        return max_depth

    left_depth = max_depth_sol(root.left)
    right_depth = max_depth_sol(root.right)
    max_depth = max(left_depth, right_depth) + 1

    return max_depth


root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)


# print(first_solution(root))
print(max_depth_sol(root))

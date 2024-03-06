class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def LCA(root, p, q):
    if root == None:
        return None

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if root == p or root == q:
        return root
    elif left and right:
        return root
    return left or right


root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

print(LCA(root, root.left.left, root.left.right.right).value)

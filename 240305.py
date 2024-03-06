import heapq
from collections import deque

graph = {
    1: [(2, 2), (1, 4)],
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    6: [(3, 5)],
    7: [(7, 6), (9, 8)],
    8: [],
}


def dijkstra(graph, start, final):
    costs = {}
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))
    return costs[final]


print(dijkstra(graph, 1, 8))


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

tree_dfs_visited = []
tree_bfs_visited = []


def tree_bfs(root):
    q = deque()
    q.append(root)

    while q:
        cur_node = q.popleft()
        tree_bfs_visited.append(root.value)
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return tree_bfs_visited


def tree_dfs(root):
    if root is None:
        return None

    tree_dfs_visited.append(root.value)
    tree_dfs(root.left)
    tree_dfs(root.right)

    return tree_dfs_visited


print(tree_bfs(root))
print(tree_dfs(root))

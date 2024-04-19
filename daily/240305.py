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
            costs[cur_v] = cur_cost
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


graph = {
    "A": ["B", "D", "E"],
    "B": ["A", "C", "D"],
    "C": ["B"],
    "D": ["A", "B"],
    "E": ["A"],
}


graph_bfs_visited = []
graph_dfs_visited = []


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
                q.append(x)
                graph_bfs_visited.append(x)

    return graph_bfs_visited


print(graph_dfs("A"))
print(graph_bfs("A"))


grid = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]


def number_of_islands(grid):
    count = 0
    row = len(grid)
    col = len(grid[0])

    visited = [[False] * col for _ in range(row)]

    def bfs(x, y):
        q = deque()
        q.append((x, y))

        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            cur_x, cur_y = q.popleft()

            for dx, dy in delta:
                next_x, next_y = cur_x + dx, cur_y + dy

                if (
                    next_x >= 0
                    and next_x < row
                    and next_y >= 0
                    and next_y < col
                    and grid[next_x][next_y] == 1
                    and visited[next_x][next_y] == False
                ):
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = True

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)
                count += 1

    return count


print(number_of_islands(grid))


# grid = [
#     [0, 0, 0],
#     [1, 1, 0],
#     [1, 1, 0],
# ]
grid = [
    [0, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
]


def shortest_path(grid):
    row = len(grid)
    col = len(grid[0])

    visited = [[False] * col for _ in range(row)]

    def bfs(x, y):
        ans = -1

        delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        q = deque()

        q.append((x, y, 1))

        while q:
            cur_x, cur_y, cur_l = q.popleft()

            if cur_x == row - 1 and cur_y == col - 1:
                return cur_l

            for dx, dy in delta:
                next_x, next_y, next_l = cur_x + dx, cur_y + dy, cur_l + 1

                if (
                    next_x >= 0
                    and next_x < row
                    and next_y >= 0
                    and next_y < col
                    and visited[next_x][next_y] == False
                    and grid[next_x][next_y] == 0
                ):
                    q.append((next_x, next_y, next_l))
                    visited[next_x][next_y] = True

        return ans

    ans = bfs(0, 0)
    return ans


print(shortest_path(grid))

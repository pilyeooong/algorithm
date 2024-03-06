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

tree_dfs_visited = []


def tree_bfs(root):
    tree_bfs_visited = []
    q = deque()
    q.append(root)

    while q:
        cur_node = q.popleft()
        tree_bfs_visited.append(cur_node.value)
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

graph_dfs_visited = []
graph_bfs_visited = []


def graph_bfs(start_v):
    q = deque()
    q.append(start_v)
    graph_bfs_visited.append(start_v)

    while q:
        cur_v = q.popleft()
        for x in graph[cur_v]:
            if x not in graph_bfs_visited:
                q.append(x)
                graph_bfs_visited.append(x)
    return graph_bfs_visited


def graph_dfs(start_v):
    graph_dfs_visited.append(start_v)

    for x in graph[start_v]:
        if x not in graph_dfs_visited:
            graph_dfs(x)
    return graph_dfs_visited


print(graph_bfs("A"))
print(graph_dfs("E"))

grid = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]


def number_of_islands(grid):
    count = 0
    row = len(grid)
    col = len(grid[0])

    visited = [[False] * col for _ in range(row)]

    def bfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        q = deque()
        q.append((x, y))
        while q:
            cur_x, cur_y = q.popleft()

            for i in range(4):
                next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                if (
                    next_x < row
                    and next_x >= 0
                    and next_y < col
                    and next_y >= 0
                    and visited[next_x][next_y] == False
                    and grid[next_x][next_y] == 1
                ):
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = True

    for i in range(row):
        for j in range(col):
            if visited[i][j] == False and grid[i][j] == 1:
                bfs(i, j)
                count += 1
    return count


grid = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]


def shortest_path(grid):
    ans = -1
    row = len(grid)
    col = len(grid[0])

    visited = [[False] * col for _ in range(row)]

    q = deque()
    q.append((0, 0, 1))
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    while q:
        cur_x, cur_y, cur_l = q.popleft()
        if cur_x == row - 1 and cur_y == col - 1:
            ans = cur_l
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


print(number_of_islands(grid))
print(shortest_path(grid))

from collections import deque

grid = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]


def number_of_ice_cream(grid):
    row = len(grid)
    col = len(grid[0])

    visited = [[False] * col for _ in range(row)]

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(x, y):
        q = deque()

        q.append((x, y))
        visited[x][y] == True

        while q:
            cur_x, cur_y = q.popleft()

            for dx, dy in delta:
                next_x, next_y = cur_x + dx, cur_y + dy

                if (
                    next_x >= 0
                    and next_x < row
                    and next_y >= 0
                    and next_y < col
                    and visited[next_x][next_y] == False
                    and grid[next_x][next_y] == 0
                ):
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = True

    count = 0
    for x in range(row):
        for y in range(col):
            if (
                x >= 0
                and x < row
                and y >= 0
                and y < col
                and grid[x][y] == 0
                and visited[x][y] == False
            ):
                bfs(x, y)
                count += 1

    return count


def dfs(grid):
    row = len(grid)
    col = len(grid[0])

    visited = [[False] * col for _ in range(row)]

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y):
        if x < 0 or x >= row or y < 0 or y >= col:
            return False

        if visited[x][y] == False and grid[x][y] == 0:
            visited[x][y] = True
            for dx, dy in delta:
                next_x, next_y = x + dx, y + dy
                dfs(next_x, next_y)
            return True
        return False

    count = 0
    for x in range(row):
        for y in range(col):
            if (
                x >= 0
                and x < row
                and y >= 0
                and y < col
                and grid[x][y] == 0
                and visited[x][y] == False
            ):
                result = dfs(x, y)
                if result == True:
                    count += 1

    return count


print(number_of_ice_cream(grid))
print(dfs(grid))

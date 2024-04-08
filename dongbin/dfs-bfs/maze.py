from collections import deque

grid = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]


def solution(grid):
    row = len(grid)
    col = len(grid[0])

    visited = [[False] * col for _ in range(row)]

    q = deque()

    q.append((0, 0, 1))
    visited[0][0] = True

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
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
                and grid[next_x][next_y] == 1
            ):
                q.append((next_x, next_y, next_l))
                visited[next_x][next_y] = True
    return 0


print(solution(grid))

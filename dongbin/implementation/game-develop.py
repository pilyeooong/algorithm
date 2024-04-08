from collections import deque

n, m = 4, 4
x, y = 1, 1
d = 0

grid = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]


def solution(grid, x, y, d):
    row = len(grid)
    col = len(grid[0])
    delta = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

    visited = [[False] * len(grid[0]) for _ in range(len(grid))]

    def turn_left(d):
        d -= 1
        if d < 0:
            d = 3
        return d

    def go_back(d):
        d = d - 2

        if d == -1:
            d = 3
        elif d == -2:
            d = 2
        return d

    count = 1
    turn_count = 0
    visited[x][y] = True
    cur_x, cur_y = x, y

    while True:
        d = turn_left(d)
        dx, dy = delta[d]

        next_x, next_y = cur_x + dx, cur_y + dy
        if (
            next_x >= 0
            and next_x < row
            and next_y >= 0
            and next_y < col
            and visited[next_x][next_y] == False
            and grid[next_x][next_y] == 0
        ):
            count += 1
            visited[next_x][next_y] = True
            cur_x, cur_y = next_x, next_y
            turn_count = 0
            continue
        else:
            turn_count += 1

        if turn_count == 4:
            back_delta = go_back(d)
            dx, dy = delta[back_delta]
            next_x, next_y = cur_x + dx, cur_y + dy
            if (
                next_x >= 0
                and next_x < row
                and next_y >= 0
                and next_y < col
                and grid[next_x][next_y] == 0
            ):
                cur_x, cur_y = next_x, next_y
                turn_count = 0
            else:
                break
    return count


print(solution(grid, x, y, d))

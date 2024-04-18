from collections import deque
import sys

# r, c = 4, 4
# grid = [
#     ["#", "#", "#", "#"],
#     ["#", "J", "F", "#"],
#     ["#", ".", ".", "#"],
#     ["#", ".", ".", "#"],
# ]

# 불이 여러개인 케이스가 커버가 안되고 있었음
# ex) 3 3
#     F.F
#     .J.
#     F.F

input = sys.stdin.readline

r, c = map(int, input().split())
grid = []
for i in range(r):
    l = list(input())
    grid.append(l)


def solution(row, col, grid):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    j_visited = [[-1] * col for _ in range(row)]
    f_visited = [[-1] * col for _ in range(row)]
    f_q = deque()
    j_q = deque()

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "J":
                j_position = (i, j)
                j_q.append(j_position)
                j_visited[j_position[0]][j_position[1]] = 0
            if grid[i][j] == "F":
                f_position = (i, j)
                f_q.append(f_position)
                f_visited[f_position[0]][f_position[1]] = 0

    while f_q:
        cur_x, cur_y = f_q.popleft()
        for dx, dy in delta:
            next_x, next_y = cur_x + dx, cur_y + dy
            if (
                next_x >= 0
                and next_x < row
                and next_y >= 0
                and next_y < col
                and grid[next_x][next_y] != "#"
                and f_visited[next_x][next_y] == -1
            ):
                f_q.append((next_x, next_y))
                f_visited[next_x][next_y] = f_visited[cur_x][cur_y] + 1

    while j_q:
        cur_x, cur_y = j_q.popleft()
        for dx, dy in delta:
            next_x, next_y = cur_x + dx, cur_y + dy
            if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                if grid[next_x][next_y] != "#" and j_visited[next_x][next_y] == -1:
                    if (
                        f_visited[next_x][next_y] == -1
                        or f_visited[next_x][next_y] > j_visited[cur_x][cur_y] + 1
                    ):
                        j_q.append((next_x, next_y))
                        j_visited[next_x][next_y] = j_visited[cur_x][cur_y] + 1
            else:
                return j_visited[cur_x][cur_y] + 1

    return "IMPOSSIBLE"


res = solution(r, c, grid)
print(res)

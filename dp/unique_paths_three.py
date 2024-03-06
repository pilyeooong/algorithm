from collections import deque

# -1 = 못감
# 0 = 지나가기 가능
# 1 = 시작점
# 2 = 도착
obstacle_grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]


def solution(obstacle_grid):
    row_len = len(obstacle_grid)
    col_len = len(obstacle_grid[0])

    start_point_row = -1
    start_point_col = -1
    for i in range(len(obstacle_grid)):
        if 1 in obstacle_grid[i]:
            start_point_row = i
    start_point_col = obstacle_grid[start_point_row].index(1)

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = [[False] * col_len for _ in range(row_len)]

    vistable_grid_count = 0
    for l in obstacle_grid:
        vistable_grid_count += l.count(0)
        vistable_grid_count += l.count(2)

    def dfs(x, y, l):
        cnt = 0
        if obstacle_grid[x][y] == 2 and l == vistable_grid_count:
            cnt += 1
        visited[x][y] = True
        for dx, dy in delta:
            next_x, next_y, next_l = x + dx, y + dy, l + 1
            if (
                next_x >= 0
                and next_x < row_len
                and next_y >= 0
                and next_y < col_len
                and obstacle_grid[next_x][next_y] != -1
                and visited[next_x][next_y] == False
            ):
                cnt += dfs(next_x, next_y, next_l)
        visited[x][y] = False

        return cnt

    ans = dfs(start_point_row, start_point_col, 0)

    return ans


print(solution(obstacle_grid))

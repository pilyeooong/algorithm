# obstacle_grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# obstacle_grid = [[0, 0], [1, 1], [0, 0]]
obstacle_grid = [[0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# obstacle_grid = [
#     [0, 1, 0, 0, 0],
#     [1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]]
# 0 0
# 1 1
# 0 0


def solution(grid):
    m = len(grid)
    n = len(grid[0])
    if obstacle_grid[0][0] == 1 or obstacle_grid[m - 1][n - 1] == 1:
        return 0

    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        if i == 0 and obstacle_grid[i][0] == 0:
            dp[i][0] = 1
        else:
            if obstacle_grid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

    for i in range(n):
        if i == 0 and obstacle_grid[0][i] == 0:
            dp[0][i] = 1
        else:
            if obstacle_grid[0][i] == 0:
                dp[0][i] = dp[0][i - 1]

    for i in range(1, m):
        for j in range(1, n):
            if obstacle_grid[i][j] != 1:
                dp[i][j] += dp[i - 1][j]
            if obstacle_grid[i][j] != 1:
                dp[i][j] += dp[i][j - 1]

    return dp[m - 1][n - 1]


print(solution(obstacle_grid))


# 1 1
# 0 0
# 1 1

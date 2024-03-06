def unique_paths(m, n):
    grid = [[0] * n for _ in range(m)]

    for i in range(m):
        grid[i][0] = 1
    for i in range(n):
        grid[0][i] = 1

    for x in range(1, m):
        for y in range(1, n):
            grid[x][y] = grid[x - 1][y] + grid[x][y - 1]

    return grid[m - 1][n - 1]


m = 3
n = 7


def dfs(r, c):
    if r == 2 and c == 6:
        return 1
    count = 0
    if r + 1 < m:
        count += dfs(r + 1, c)
    if c + 1 < n:
        count += dfs(r, c + 1)

    return count


def top_down(m, n):
    memo = [[-1] * n for _ in range(m)]

    def dfs(r, c):
        if r == 0 and c == 0:
            memo[r][c] = 1
            return memo[r][c]

        count = 0
        if memo[r][c] == -1:
            if r - 1 >= 0:
                count += dfs(r - 1, c)
            if c - 1 >= 0:
                count += dfs(r, c - 1)
            memo[r][c] = count
        return memo[r][c]

    return dfs(m - 1, n - 1)


def top_down_dfs(r, c):
    if r == 1 and c == 1:
        return 1

    count = 0
    if r - 1 >= 1:
        count += top_down_dfs(r - 1, c)
    if c - 1 >= 1:
        count += top_down_dfs(r, c - 1)

    return count


# print(unique_paths(m, n))
# print(dfs(0, 0))
print(top_down(3, 7))
print(top_down_dfs(3, 7))
# 1 1 1
# 1 2 3
# 1 3 6

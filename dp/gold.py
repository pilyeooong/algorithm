n = 3
m = 4

grid = [[1, 3, 3, 2], [2, 1, 4, 1], [0, 6, 4, 7]]


def solution(grid):
    delta = [(0, -1), (-1, -1), (1, -1)]

    row = len(grid)
    col = len(grid[0])

    dp = [[0] * col for _ in range(row)]

    for i in range(row):
        dp[i][0] = grid[i][0]

    for i in range(row):
        for j in range(1, col):
            biggest = 0
            for dx, dy in delta:
                x, y = i + dx, j + dy
                if x >= 0 and x < row and y >= 0 and y < col:
                    biggest = max(biggest, dp[x][y])
            dp[i][j] += grid[i][j] + biggest

    return max([element for sub_list in dp for element in sub_list])


print(solution(grid))

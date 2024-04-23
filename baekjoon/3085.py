# n = 3

# grid = [["C", "C", "P"], ["C", "C", "P"], ["P", "P", "C"]]

# 4
# CPZY
# CPZZ
# ZYCC
# CCYC

n = int(input())
grid = []
for _ in range(n):
    grid.append(list(input()))


def solution(grid):
    row = len(grid)
    col = len(grid[0])

    def check(grid):
        row = len(grid)
        col = len(grid[0])

        row_cnt = 1
        for i in range(row):
            cnt = 1
            for j in range(col - 1):
                if grid[i][j] == grid[i][j + 1]:
                    cnt += 1
                else:
                    cnt = 1
                row_cnt = max(row_cnt, cnt)

        col_cnt = 1
        for i in range(row):
            cnt = 1
            for j in range(col - 1):
                if grid[j][i] == grid[j + 1][i]:
                    cnt += 1
                else:
                    cnt = 1
                col_cnt = max(cnt, col_cnt)

        ans = max(row_cnt, col_cnt)

        return ans

    ans = check(grid)
    for i in range(row):
        for j in range(col - 1):
            grid[i][j], grid[i][j + 1] = grid[i][j + 1], grid[i][j]
            cnt = check(grid)
            ans = max(cnt, ans)
            grid[i][j], grid[i][j + 1] = grid[i][j + 1], grid[i][j]
    for i in range(row):
        for j in range(col - 1):
            grid[j][i], grid[j + 1][i] = grid[j + 1][i], grid[j][i]
            cnt = check(grid)
            ans = max(cnt, ans)
            grid[j][i], grid[j + 1][i] = grid[j + 1][i], grid[j][i]

    return ans


print(solution(grid))

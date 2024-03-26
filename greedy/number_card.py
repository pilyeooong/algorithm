n, m = 3, 3
grid = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]


def solution(grid):
    l = []
    for i in range(len(grid)):
        l.append(min(grid[i]))

    return max(l)


print(solution(grid))

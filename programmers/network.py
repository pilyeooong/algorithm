from collections import deque


def solution(n, computers):
    answer = 0

    row = len(computers)
    col = len(computers[0])

    visited = [False] * n

    def dfs(x):
        visited[x] = True

        for i in range(n):
            if visited[i] == False and computers[x][i] == 1:
                dfs(i)
        return

    for x in range(row):
        for y in range(col):
            if computers[x][y] == 1 and visited[x] == False:
                dfs(x)
                answer += 1

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [
#     [1, 1, 0],
#     [1, 1, 0],
#     [0, 0, 1]
# ]

# computers = [[1, 1, 0, 0], [1, 1, 0, 1], [0, 0, 1, 0], [0, 0, 1, 0]]


print(solution(n, computers))

from collections import deque
import copy

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"

# board = [
#     ["A", "B", "C", "E"],
#     ["S", "F", "E", "S"],
#     ["A", "D", "E", "E"]
#     ]
word = "ABCESEEEFS"
board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]


def solution(board, word):
    global answer
    answer = False
    row = len(board)
    col = len(board[0])

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y, find_idx, visited):
        global answer

        if find_idx == len(word):
            answer = True
            return

        for dx, dy in delta:
            next_x, next_y = x + dx, y + dy
            if (
                next_x >= 0
                and next_x < row
                and next_y >= 0
                and next_y < col
                and visited[next_x][next_y] == 0
                and board[next_x][next_y] == word[find_idx]
            ):
                visited[next_x][next_y] = 1
                dfs(next_x, next_y, find_idx + 1, visited)
                visited[next_x][next_y] = 0

    visited = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            find_idx = 0
            if board[i][j] == word[find_idx]:
                visited[i][j] = 1
                dfs(i, j, find_idx + 1, visited)
                visited[i][j] = 0
    return answer


print(solution(board, word))

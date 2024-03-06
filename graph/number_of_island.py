from collections import deque

# grid = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]


def solution(grid):
    number_of_islands = 0

    row = len(grid)
    col = len(grid[0])

    # 방문 여부 체크를 위한 visited 배열 생성, 특정 지점의 방문여부 체크를 위해 False로 이루어진 배열로 사전 초기화
    visited = [[False] * col for _ in range(row)]

    def bfs(x, y):
        dx = [-1, 1, 0, 0]  # 상하좌우의 순서 , row
        dy = [0, 0, -1, 1]  # col

        q = deque()
        q.append((x, y))
        visited[x][y] = True

        while q:
            cur_x, cur_y = q.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if (
                    next_x >= 0
                    and next_y >= 0
                    and next_x < row
                    and next_y < col
                    and grid[next_x][next_y] == 1
                    and visited[next_x][next_y] == False
                ):
                    visited[next_x][next_y] = True
                    q.append((next_x, next_y))

    for x in range(row):
        for y in range(col):
            if visited[x][y] == False and grid[x][y] == 1:
                bfs(x, y)
                number_of_islands += 1

    return number_of_islands


def number_of_islands(grid):
    number_of_islands = 0
    row = len(grid)
    col = len(grid[0])

    visited = [[False] * col for _ in range(row)]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True

        dx = [-1, 1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, -1, 1, -1, 1, -1, 1]

        while q:
            cur_x, cur_y = q.popleft()
            for i in range(8):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]

                if (
                    next_x < row
                    and next_x >= 0
                    and next_y < col
                    and next_y >= 0
                    and not visited[next_x][next_y]
                    and grid[next_x][next_y] == 1
                ):
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = True

    for i in range(row):
        for j in range(col):
            if visited[i][j] == False and grid[i][j] == 1:
                bfs(i, j)
                number_of_islands += 1

    return number_of_islands


print(number_of_islands(grid))

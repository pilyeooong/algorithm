from collections import deque
def bracket(string):
    q = deque()

    for s in string:
        if s == "(":
            q.append(")")
        elif s == "[":
            q.append("]")
        elif s == "{":
            q.append("}")
        elif not q or q.pop() != s:
                return False
    return True

result = bracket("()()()")
print(result)

# grid = [
#      [1, 1, 1, 1, 0],
#      [1, 1, 0, 1, 0],
#      [1, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0]
# ]

grid = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1]]

def islands(grid):
    row = len(grid)
    col = len(grid[0])
    count = 0

    visited = [[False] * col for _ in range(row)]

    def bfs(x, y):
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        q.append((x, y))

        while q:
             cur_x, cur_y = q.popleft()
             for dx, dy in deltas:
                  next_x, next_y = cur_x + dx, cur_y + dy
                  if next_x < row and next_x >= 0 and next_y < col and next_y >= 0 and visited[next_x][next_y] == False and grid[next_x][next_y] == 1:
                       q.append((next_x, next_y))
                       visited[next_x][next_y] = True
    
    for x in range(row):
         for y in range(col):
              if visited[x][y] == False and grid[x][y] == 1:
                   bfs(x, y)
                   count += 1
    
    return count

result = islands(grid)
print(result)

grid = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]


def shortest_path(grid):
    ans = -1
    row = len(grid)
    col = len(grid[0])

    visited = [[False] * col for _ in range(row)]

    q = deque()
    q.append((0, 0, 1))
    deltas = [(-1, 0), (1, 0),(0, -1), (0, 1), (-1,-1), (-1, 1),(1, -1), (1, 1)]

    while q:
        cur_x, cur_y, cur_l = q.popleft()

        if cur_x == row - 1 and cur_y == col - 1:
            ans = cur_l
        for dx, dy in deltas:
            next_x, next_y, next_l = cur_x + dx, cur_y + dy, cur_l + 1

            if next_x < row and next_x >= 0 and next_y < col and next_y <= 0 and visited[next_x][next_y] == False and grid[next_x][next_y] == 0:
                q.append((next_x, next_y, next_l))
                visited[next_x][next_y] = True
    
    return ans


result = shortest_path(grid)
print(result)

from collections import deque
import heapq

graph = {
    1: [(2, 2), (1, 4)],
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    6: [(3, 5)],
    7: [(7, 6), (9, 8)],
    8: [],
}


def dijkstra(graph, start, final):
    costs = {}
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cost + cur_cost
                heapq.heappush(pq, (next_cost, next_v))

    return costs[final]


print(dijkstra(graph, 1, 8))


grid = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]


def number_of_islands(grid):
    row = len(grid)
    col = len(grid[0])

    visited = [[False] * col for _ in range(row)]

    count = 0

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q:
            cur_x, cur_y = q.popleft()

            for dx, dy in delta:
                next_x, next_y = cur_x + dx, cur_y + dy
                if (
                    next_x >= 0
                    and next_x < row
                    and next_y >= 0
                    and next_y < col
                    and visited[next_x][next_y] == False
                    and grid[next_x][next_y] == 1
                ):
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = True

    for i in range(row):
        for j in range(col):
            if visited[i][j] == False and grid[i][j] == 1:
                bfs(i, j)
                count += 1
    return count


print(number_of_islands(grid))

s = "1234567876543"


def longest_palindrome(s):
    if len(s) < 2 or s == s[::-1]:
        return s

    def expand(left, right):
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1 : right - 1]

    result = ""
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result


print(longest_palindrome(s))

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def trapping_rain_water(height):
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    volume = 0
    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume


print(trapping_rain_water(height))

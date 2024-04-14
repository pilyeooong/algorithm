from collections import deque


def solution(n, start, finish):
    delta = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (2, 1), (1, 2)]

    visited = [[False] * n for _ in range(n)]

    q = deque()
    q.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True

    while q:
        cur_x, cur_y, cur_l = q.popleft()
        if cur_x == finish[0] and cur_y == finish[1]:
            return cur_l
        for dx, dy in delta:
            next_x, next_y, next_l = cur_x + dx, cur_y + dy, cur_l + 1
            if (
                next_x >= 0
                and next_x < n
                and next_y >= 0
                and next_y < n
                and visited[next_x][next_y] == False
            ):
                q.append((next_x, next_y, next_l))
                visited[next_x][next_y] = True


n = int(input())
for i in range(n):
    x = int(input())
    start = list(map(int, input().split()))
    finish = list(map(int, input().split()))
    print(solution(x, start, finish))

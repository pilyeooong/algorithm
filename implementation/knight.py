s = "c2"


def solution(s):
    grid = [[False] * 8 for _ in range(8)]
    delta = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, 1), (-2, -1), (2, -1), (2, 1)]

    dic = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
    }
    x = dic[s[0]]
    y = int(s[1]) - 1

    count = 0

    for dx, dy in delta:
        next_x, next_y = x + dx, y + dy
        if next_x >= 0 and next_x < len(grid) and next_y >= 0 and next_y < len(grid[0]):
            count += 1

    return count


print(solution(s))

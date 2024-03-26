n = 5
l = ["R", "R", "R", "U", "D", "D"]


def solution(n, l):
    delta = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    cur_x, cur_y = 1, 1

    for d in l:
        dx, dy = delta[d]
        next_x, next_y = cur_x + dx, cur_y + dy

        if next_x >= 1 and next_y >= 1:
            cur_x, cur_y = next_x, next_y

    return cur_x, cur_y


print(solution(n, l))

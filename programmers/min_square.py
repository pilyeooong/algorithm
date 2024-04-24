sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]


def solution(sizes):
    answer = 0

    w = []
    h = []

    for size in sizes:
        w.append(max(size))
        h.append(min(size))
    answer = max(w) * max(h)
    return answer


print(solution(sizes))

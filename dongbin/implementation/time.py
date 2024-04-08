n = 5


def solution(n):
    t = ""
    count = 0
    for h in range(n + 1):
        for m in range(60):
            for s in range(60):
                t = f"{h}{m}{s}"
                if "3" in t:
                    count += 1

    return count


print(solution(n))

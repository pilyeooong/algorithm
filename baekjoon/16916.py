s = "baekjoon"
p = "oone"

s = input()
p = input()


def solution(s, p):
    if p in s:
        return 1
    return 0


print(solution(s, p))

s = "baekjoon"
p = "oone"


def solution(s, p):
    i = 0
    while i < len(s):
        if s[i] == p[0]:
            if s[i : i + len(p)] == p:
                return 1
        i += 1
    return 0


print(solution(s, p))

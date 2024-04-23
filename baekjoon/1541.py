s = "-10+20+30+40"


def solution(s):
    ss = list(filter(lambda x: len(x) > 0, s.split("-")))

    answer = 0
    t = sum(list(map(int, ss[0].split("+"))))
    if s[0] == "-":
        answer -= t
    else:
        answer += t
    for i in ss[1:]:
        t = sum(list(map(int, i.split("+"))))
        answer -= t
    return answer


# s = input()
print(solution(s))

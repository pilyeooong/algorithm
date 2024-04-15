from collections import Counter

s = "cbaebabacd"
p = "abc"


def solution(s, p):
    ans = []
    sp = Counter(p)
    print(sp)
    for i in range(len(s) - len(p) + 1):
        sliced = s[i : i + len(p)]

        if sp == Counter(sliced):
            ans.append(i)

    return ans


print(solution(s, p))

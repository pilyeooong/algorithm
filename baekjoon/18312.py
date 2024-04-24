n, k = map(int, input().split())


def solution(n, k):
    ans = 0
    for h in range(0, n + 1):
        for m in range(0, 60):
            for s in range(0, 60):
                if h < 10:
                    str_h = "0" + str(h)
                else:
                    str_h = str(h)
                if m < 10:
                    str_m = "0" + str(m)
                else:
                    str_m = str(m)
                if s < 10:
                    str_s = "0" + str(s)
                else:
                    str_s = str(s)
                if str(k) in (str_h + str_m + str_s):
                    ans += 1
    return ans


print(solution(n, k))

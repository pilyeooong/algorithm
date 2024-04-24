n = 5
l = [2, 3, 1, 2, 2]


def solution(n, l):
    l.sort()

    ans = 0
    cnt = 0
    for i in l:
        cnt += 1
        if cnt >= i:
            ans += 1
            cnt = 0
    return ans


print(solution(n, l))

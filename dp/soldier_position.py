l = [15, 11, 4, 8, 5, 2, 4]


# lds
def solution(l):
    dp = [1] * len(l)

    for i in range(1, len(l)):
        for j in range(i):
            if l[i] < l[j]:
                dp[i] = max(dp[j] + 1, dp[i])

    print(dp)


# lis 가장 긴 부분수열의 길이
def solution2(l):
    dp = [1] * len(l)

    l.reverse()

    for i in range(1, len(l)):
        for j in range(i):
            if l[j] < l[i]:
                dp[i] = max(dp[j] + 1, dp[i])
    print(dp)


solution(l)
solution2(l)


l = [15, 11, 4, 8, 5, 2, 4]


def solution3(l):
    dp = [1] * len(l)

    for i in range(1, len(l)):
        for j in range(i):
            if l[i] < l[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return len(l) - max(dp)


print(solution3(l))

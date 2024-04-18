def solution(n, m, l):
    dp = [10001] * (m + 1)

    for i in range(1, m + 1):
        if i in l:
            dp[i] = 1
        else:
            for x in l:
                if i - x > 0 and dp[i - x] != 0:
                    dp[i] = min(dp[i], dp[i - x] + 1)
    if dp[m] == 10001:
        return -1
    else:
        return dp[m]


n = 2
m = 15
l = [2, 3]

print(solution(n, m, l))
print(solution(3, 4, [3, 5, 7]))


def solution2(n, m, l):
    dp = [10001] * (m + 1)

    for i in l:
        dp[i] = 1

    for i in range(1, m + 1):
        if i in l:
            dp[i] = 1
        else:
            for x in l:
                if i - x > 0:
                    dp[i] = min(dp[i], dp[i - x] + 1)
    print(dp)


print(solution2(n, m, l))

def solution(x):
    dp = [0 for _ in range(30)]

    for i in range(2, x + 1):
        dp[i] = dp[i - 1] + 1
        if i % 5 == 0:
            dp[i] = min(dp[i // 5] + 1, dp[i])
        if i % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i])
        if i % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i])
    return dp[x]


x = 26
print(solution(x))


n, k = 25, 5


def solution(n, k):
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % k == 0:
            dp[i] = min(dp[i // k] + 1, dp[i])

    return dp[n]


print(solution(n, k))

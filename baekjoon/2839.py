n = int(input())


def solution(n):
    l = [3, 5]

    dp = [5001] * (n + 1)

    for i in range(n + 1):
        if i in l:
            dp[i] = 1

        for x in l:
            if i - x > 0:
                dp[i] = min(dp[i - x] + 1, dp[i])
    if dp[n] == 5001:
        print(-1)
    else:
        print(dp[n])


solution(n)

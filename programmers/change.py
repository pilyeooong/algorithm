n = 5
money = [1, 2, 5]


def solution(n, money):
    money.sort()

    dp = [0] * (n + 1)
    dp[0] = 1  # money의 최소값은 1로 초기화 (아래 i-m 부분에서)

    for m in money:
        for i in range(m, n + 1):
            dp[i] += dp[i - m]
    return dp[n]


print(solution(n, money))

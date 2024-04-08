# n 은 가로 길이, 세로는 2로 고정
def solution(n):
    dp = [0] * 10000
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = dp[i - 2] * 2 + dp[i - 1]
    return dp[n]


print(solution(3))

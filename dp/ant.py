n = 3
arr = [1, 2, 3]


def solution(n, arr):
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
        print(dp)

    return max(dp)


print(solution(n, arr))

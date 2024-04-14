l = [10, 30, 10, 20, 20, 10]


n = int(input())
l = list(map(int, input().split()))


def solution(l):
    dp = [1] * len(l)

    for i in range(1, len(l)):
        for j in range(i):
            if l[j] > l[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


print(solution(l))

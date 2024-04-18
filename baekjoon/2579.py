n = int(input())
l = []
for _ in range(n):
    x = int(input())
    l.append(x)


def solution(l):
    if len(l) < 3:
        print(sum(l))
    else:
        dp = [0] * len(l)
        dp[0] = l[0]
        dp[1] = l[0] + l[1]
        dp[2] = max(l[0] + l[2], l[1] + l[2])

        for i in range(3, len(l)):
            dp[i] = max(l[i] + l[i - 1] + dp[i - 3], l[i] + dp[i - 2])

        print(dp[-1])


solution(l)

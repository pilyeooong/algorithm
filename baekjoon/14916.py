n = int(input())

money = [2, 5]
money.sort(reverse=True)

dp = [100001] * (n + 1)

for i in range(1, n + 1):
    for m in money:
        if i == m:
            dp[i] = 1
        else:
            if i - m >= 0:
                dp[i] = min(dp[i], dp[i - m] + 1)

result = dp[-1]
if result == 100001:
    print(-1)
else:
    print(result)

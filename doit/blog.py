# 21921

N, M = 7, 5
visitors_count = [1, 1, 1, 1, 1, 5, 1]

N, M = map(int, input().split())
visitors_count = list(map(int, input().split()))

memo = [0] * (N - M + 1)
for i in range(N - M + 1):
    if i == 0:
        for j in range(M):
            memo[i] += visitors_count[j]
    else:
        memo[i] = memo[i - 1] - visitors_count[i - 1]
        memo[i] += visitors_count[i + M - 1]

maximum_count = max(memo)
day_count = memo.count(maximum_count)

if maximum_count == 0:
    print("SAD")
else:
    print(maximum_count)
    print(day_count)

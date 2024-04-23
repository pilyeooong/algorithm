# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
l = []
for _ in range(N):
    l.append(int(input()))


def solution(l, K):
    l.sort(reverse=True)

    count = 0
    for coin in l:
        if K >= coin:
            count += K // coin
            K %= coin
    return count


print(solution(l, K))

print(l, K)

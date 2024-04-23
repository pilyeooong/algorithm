import sys

input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))


def solution(l):
    l.sort(key=lambda x: (x[1], x[0]))
    print(l)

    ans = 1
    start = l[0]
    for i in range(1, len(l)):
        if start[1] <= l[i][0]:
            start = l[i]
            ans += 1
    return ans


print(solution(l))

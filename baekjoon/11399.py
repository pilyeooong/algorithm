n = int(input())
l = list(map(int, input().split()))


def solution(n, l):
    l.sort()
    count = 0
    for i in range(1, n + 1):
        for j in range(i):
            count += l[j]
    return count


print(solution(n, l))

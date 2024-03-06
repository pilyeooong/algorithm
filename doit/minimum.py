# 11003

n, m = 12, 3
l = [1, 5, 2, 3, 6, 2, 3, 7, 3, 5, 2, 6]

n, m = map(int, input().split())
l = list(map(int, input().split()))

checker = []
for i in range(n):
    if i - m + 1 <= 0:
        checker.append(l[i])
    else:
        checker.pop(0)
        checker.append(l[i])
    print(min(checker))

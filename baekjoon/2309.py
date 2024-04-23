# l = [20, 7, 23, 19, 10, 15, 25, 8, 13]
import sys

input = sys.stdin.readline

l = []
for _ in range(9):
    l.append(int(input()))

l.sort(reverse=True)

total = sum(l)

not_l = []
for i in range(len(l)):
    check = total - l[i]
    for j in range(i + 1, len(l)):
        if check - l[j] == 100:
            not_l = [i, j]

ans = [l[i] for i in range(len(l)) if i not in not_l]
for x in ans[::-1]:
    print(x)

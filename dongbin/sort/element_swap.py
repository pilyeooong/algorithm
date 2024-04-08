a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]
k = 3


def solution(a, b, k):
    a.sort()
    b.sort(reverse=True)

    for i in range(len(a)):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
            k -= 1
        if k == 0:
            break

    return sum(a)


print(solution(a, b, k))

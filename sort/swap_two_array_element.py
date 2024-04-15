n, k = 5, 3

l1 = [1, 2, 5, 4, 3]
l2 = [1, 1, 1, 1, 1]


def solution(l1, l2, k):
    l1.sort()
    l2.sort(reverse=True)

    for i in range(k):
        if l1[i] < l2[i]:
            l1[i], l2[i] = l2[i], l1[i]
        else:
            break
    return sum(l1)


print(solution(l1, l2, k))

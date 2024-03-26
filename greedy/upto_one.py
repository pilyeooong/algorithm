n, k = 24, 5


def solution(n, k):
    count = 0
    copy = n
    while copy > 1:
        if copy % k == 0:
            copy = copy / k
        else:
            copy -= 1
        count += 1

    if copy == 1:
        return count
    else:
        return -1


print(solution(n, k))

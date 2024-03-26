# n, m, k = map(int, input().split())
# l = list(map(int, input().split()))

n, m, k = 5, 8, 3
l = [2, 4, 5, 4, 6]


def solution(n, m, k, l):
    sorted_l = sorted(l)

    first_num = sorted_l[n - 1]
    second_num = sorted_l[n - 2]

    count = k

    total = 0
    for _ in range(m):
        if count > 0:
            total += first_num
            count -= 1
        else:
            total += second_num
            count = k

    return total


def solution2(n, m, k, l):
    sorted_l = sorted(l)

    first_num = sorted_l[n - 1]
    second_num = sorted_l[n - 2]

    first_num_sum_count = int(m / (k + 1)) * k
    second_num_sum_count = m - first_num_sum_count

    total = 0
    total += first_num_sum_count * first_num
    total += second_num_sum_count * second_num

    return total


print(solution(n, m, k, l))
print(solution2(n, m, k, l))

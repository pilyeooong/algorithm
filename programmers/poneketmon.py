from collections import defaultdict


def solution(nums):
    answer = 0

    select_num = int(len(nums) / 2)
    set_nums = set(nums)

    if len(set_nums) < select_num:
        return int(len(set_nums))

    if select_num <= len(set_nums):
        return select_num

    return answer


nums = [3, 1, 2, 3]
print(solution(nums))

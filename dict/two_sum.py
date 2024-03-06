def solution(nums, target):
    dict = {}
    for num in nums:
        dict[num] = True

    for num in nums:
        if target - num in dict and target - num != num:
            return True
    return False


nums = [4, 1, 9, 7, 8, 2]
target = 14

print(solution(nums, target))

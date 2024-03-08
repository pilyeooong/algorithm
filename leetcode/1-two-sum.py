nums = [2, 7, 11, 15]
target = 9
nums = [2, 3, 4]
target = 6


def solution(nums, target):
    for i, n in enumerate(nums):
        find_num = target - n
        if find_num in nums[i + 1 :]:
            ans = [i, nums[i + 1 :].index(find_num) + i + 1]
            return ans
    return []


def two_pointer(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        if target == nums[left] + nums[right]:
            return [left, right]
        elif target < nums[left] + nums[right]:
            right -= 1
        elif target > nums[left] + nums[right]:
            left += 1
    return [-1, -1]


print(two_pointer(nums, target))


nums = [3, 4, 5, 6, 7, 8, 9, 10]
target = 10

def binary_search(nums, target):
    nums.sort()

    left = 0
    right = len(nums) - 1
    pivot = len(nums) // 2
    count = 0

    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return count
        elif nums[pivot] < target:
            left = pivot + 1
        else:
            right = pivot - 1
        count += 1

    return count

print(binary_search(nums, target))
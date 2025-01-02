#       l           p         r
nums = [3, 4, 5, 6, 7, 8, 9, 10]
target = 8

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] < target:
            left = pivot + 1
        else:
            right = pivot - 1

    return None
print(binary_search(nums, target))

# nums = [-1,0,1,2,-1,-4]
# [[-1,-1,2],[-1,0,1]]

nums = [-1,0,1,2,-1,-4]

def three_sum(nums):
    nums.sort()
    ans = []

    for i in range(len(nums)):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in ans:
                    ans.append([nums[i], nums[j], nums[k]]) 
    return ans

print(three_sum(nums))
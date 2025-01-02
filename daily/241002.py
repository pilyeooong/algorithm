def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False

print(two_sum(nums=[4,1,9,7,5,3,17], target=14))

def two_sum2(nums, target):
    nums.sort()
    print(nums)
    for i in range(len(nums)-1):
        if target - nums[i] in nums[i+1::]:
            return True
    return False

print(two_sum2(nums=[4,1,9,7,5,3,17], target=14))

def two_pointer_sum(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1

    while True:
        if nums[left] + nums[right] == target:
            return True

        if nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
        
        if left >= right:
            break

    return False

print(two_pointer_sum(nums=[2,1,5,7], target=4))

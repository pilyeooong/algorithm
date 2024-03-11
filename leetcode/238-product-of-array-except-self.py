nums = [1, 2, 3, 4]
# [24, 12, 8 ,6]


def solution(nums):
    ans = []
    for i in range(len(nums)):
        if i == 0:
            total = 1
            for j in nums[i + 1 :]:
                total *= j
            ans.append(total)
        else:
            total = 1
            for j in range(i + 1, len(nums)):
                total *= nums[j]
            for j in range(i - 1, -1, -1):
                total *= nums[j]
            ans.append(total)

    return ans


print(solution(nums))

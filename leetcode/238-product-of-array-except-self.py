nums = [1, 2, 3, 4]
# [24, 12, 8 ,6]


# timeout
# def solution(nums):
#     ans = []
#     for i in range(len(nums)):
#         if i == 0:
#             total = 1
#             for j in nums[i + 1 :]:
#                 total *= j
#             ans.append(total)
#         else:
#             total = 1
#             for j in range(i + 1, len(nums)):
#                 total *= nums[j]
#             for j in range(i - 1, -1, -1):
#                 total *= nums[j]
#             ans.append(total)

#     return ans

# def solution(nums):
#     ans = []
#     p = 1
#     for i in range(len(nums)):
#         ans.append(p)
#         p = p * nums[i]
#     p = 1
#     for i in range(len(nums) - 1, -1, -1):
#         ans[i] = ans[i] * p
#         p = p * nums[i]

#     return ans


def solution(nums):
    ans = []
    left = []
    right = []
    p = 1
    for i in range(len(nums)):
        left.append(p)
        p = p * nums[i]
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        right.append(p)
        p = p * nums[i]
    right.reverse()

    for i in range(len(nums)):
        ans.append(left[i] * right[i])
    return ans


print(solution(nums))

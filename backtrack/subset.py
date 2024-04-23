nums = [1, 2, 3, 4]


def solution(nums):
    nums_l = len(nums)
    ans = []

    def combination(start, cur, k):
        if len(cur) == k:
            ans.append(cur[:])
            return
        for i in range(start, nums_l):
            if nums[i] not in cur:
                cur.append(nums[i])
                combination(i + 1, cur, k)
                cur.pop()

    for i in range(nums_l + 1):
        combination(0, [], i)

    return ans


print(solution(nums))

def solution(nums, k):
    ans = []

    def backtrack(cur, start):
        if len(cur) == k:
            ans.append(cur[:])
            return

        for i in range(start, len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                backtrack(cur, i + 1)
                cur.pop()

    backtrack([], 0)

    return ans


nums = [1, 2, 3, 4]
k = 2
print(solution(nums, k))

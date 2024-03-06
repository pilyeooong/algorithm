nums = [1, 2, 3, 4]
ans = []


def backtrack(cur):
    if len(cur) == len(nums):
        ans.append(cur[:])
        return

    for num in nums:
        if num not in cur:
            cur.append(num)
            backtrack(cur)
            cur.pop()


backtrack([])
print(ans)

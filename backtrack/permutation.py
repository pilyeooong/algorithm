nums = [1, 2, 3, 4]
ans = []

# backtracking
# solution이 될 가능성이 없는 candidate는 제외(포기)하고 탐색


def backtrack(cur):
    if len(cur) == len(nums):
        ans.append(cur[:])  # deep copy
        return

    for num in nums:
        if num not in cur:
            cur.append(num)
            backtrack(cur)
            cur.pop()


def solution(cur):
    if len(cur) == len(nums):
        ans.append(cur[:])
        return

    for num in nums:
        if num not in cur:
            cur.append(num)
            backtrack(cur)
            cur.pop()


solution([])
print(ans)

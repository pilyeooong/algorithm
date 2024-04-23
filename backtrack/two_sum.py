nums = [4, 9, 7, 5, 1]
target = 9


def solution(nums, k, target):
    global answer
    answer = False

    def backtrack(start, cur):
        global answer
        if len(cur) == k and sum(cur) == target:
            answer = True
            return

        for i in range(start, len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()

    backtrack(0, [])

    return answer


print(solution(nums, 2, target))

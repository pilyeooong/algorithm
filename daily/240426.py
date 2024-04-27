l = [5, 8, 4, 1, 2, 3, 9]


def insertion_sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j - 1] > l[j]:
                l[j - 1], l[j] = l[j], l[j - 1]
    return l


print(insertion_sort(l[:]))


def selection_sort(l):
    for i in range(len(l)):
        min_idx = i
        for j in range(i + 1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
        l[min_idx], l[i] = l[i], l[min_idx]
    return l


print(selection_sort(l[:]))


def quick_sort(l, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and l[left] <= l[pivot]:
            left += 1
        while right > start and l[right] >= l[pivot]:
            right -= 1

        if left > right:
            l[pivot], l[right] = l[right], l[pivot]
        else:
            l[left], l[right] = l[right], l[left]

        quick_sort(l, start, right - 1)
        quick_sort(l, right + 1, end)

    return l


print(quick_sort(l[:], 0, len(l) - 1))

nums = [1, 2, 3, 4]


def permutation(nums):
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

    return ans


# print(permutation(nums))


def combinations(nums, k):
    ans = []

    def backtrack(start, cur):
        if len(cur) == k:
            ans.append(cur[:])
            return

        for i in range(start, len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()

    backtrack(0, [])

    return ans


print(combinations(nums, 2))


def subsets(nums):
    ans = []

    def backtrack(start, cur, k):
        if len(cur) == k:
            ans.append(cur[:])
            return

        for i in range(start, len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                backtrack(i + 1, cur, k)
                cur.pop()

    for i in range(len(nums) + 1):
        backtrack(0, [], i)

    return ans


print(subsets(nums))

import heapq


def shortest_path_in_matrix(n):
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[0][i] = 1
        dp[i][0] = 1

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n - 1][n - 1]


print(shortest_path_in_matrix(4))

l = [5, 8, 4, 1, 2, 3, 9]


def insertion_sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j - 1] > l[j]:
                l[j - 1], l[j] = l[j], l[j - 1]
    return l


print(insertion_sort(l))

l = [5, 8, 4, 1, 2, 3, 9]


def selection_sort(l):
    for i in range(len(l)):
        min_idx = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_idx]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]
    return l


print(selection_sort(l))


l = [5, 8, 4, 1, 2, 3, 9]


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
            l[right], l[pivot] = l[pivot], l[right]
        else:
            l[left], l[right] = l[right], l[left]

    quick_sort(l, start, right - 1)
    quick_sort(l, right + 1, end)

    return l


print(quick_sort(l, 0, len(l) - 1))


graph = {
    1: [(2, 2), (1, 4)],
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    6: [(3, 5)],
    7: [(7, 6), (9, 8)],
    8: [],
}


def dijkstra(graph, start, end):
    costs = {}
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cost + cur_cost
                heapq.heappush(pq, (next_cost, next_v))

    return costs[end]


print(dijkstra(graph, 1, 8))

nums = [1, 2, 3, 4]


def permutation(nums):
    ans = []

    def backtrack(cur):
        if len(cur) == len(nums):
            ans.append(cur[:])  # deep copy
            return

        for num in nums:
            if num not in cur:
                cur.append(num)
                backtrack(cur)
                cur.pop()

    backtrack([])
    return ans


print(permutation(nums))
# print(len(permutation(nums)))


def combination(nums, k):
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


print(combination(nums, 2))


def subset(nums):
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


print(subset(nums))


nums = [4, 9, 7, 5, 1]


def recursive_two_sum(nums, k, target):
    global answer
    answer = False

    def backtrack(start, cur):
        global answer
        if len(cur) == k and sum(cur) == target:
            print(cur)
            answer = True
            return

        for i in range(start, len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()

    backtrack(0, [])

    return answer


print(recursive_two_sum(nums, 3, 15))

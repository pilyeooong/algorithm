import heapq

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

nums = [0, -1]


def solution(nums):
    dic = {}
    dic = {num: num + 1 for num in nums}

    max_count = 0
    for i in dic:
        if i - 1 not in dic:
            count = 1
            next_num = dic[i]
            while next_num in dic:
                count += 1
                next_num = dic[next_num]
            max_count = max(max_count, count)
    return max_count


print(solution(nums))


l = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def insertion_sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j - 1] > l[j]:
                l[j - 1], l[j] = l[j], l[j - 1]
            else:
                break
    return l


print(insertion_sort(l))


def selection_sort(l):
    for i in range(len(l)):
        minimum_index = i
        for j in range(i + 1, len(l)):
            if l[minimum_index] > l[j]:
                minimum_index = j
        l[minimum_index], l[i] = l[i], l[minimum_index]

    return l


l = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(selection_sort(l))


l = [5, 6, 3, 4, 9, 7, 5, 1]


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


print(quick_sort(l, 0, len(l) - 1))

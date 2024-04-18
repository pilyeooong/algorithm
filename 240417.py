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

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def selection_sort(l):
    for i in range(len(l)):
        minimum_index = i
        for j in range(i, len(l)):
            if l[minimum_index] > l[j]:
                minimum_index = j
        l[minimum_index], l[i] = l[i], l[minimum_index]

    return l


def insertion_sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j - 1] > l[j]:
                l[j], l[j - 1] = l[j - 1], l[j]
            else:
                break
    return l


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
            l[left], l[right] = l[right], l[pivot]

    quick_sort(l, start, right - 1)
    quick_sort(l, right + 1, end)

    return l


print(selection_sort(array))
print(insertion_sort(array))
print(quick_sort(array, 0, len(array) - 1))

s = "111999333"


def solution(s):
    result = -1
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            result = max(result, int(s[i : i + 3]))
    return result


print(solution(s))


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    ans = []

    for i, j, k in commands:
        l = sorted(array[i - 1 : j])
        ans.append(l[k - 1])

    return ans


print(solution(array, commands))

[[-1, -1, -1, -1], [-1, 1, 0, -1], [-1, 2, 1, -1], [-1, 3, 2, -1]]

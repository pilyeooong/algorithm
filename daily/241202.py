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
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))

    return costs[end]

print(dijkstra(graph, 1, 8))


nums = [1,2,3,4,5,6,7,8,9,10]
target = 10

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return True
        if nums[pivot] > target:
            right = pivot - 1
        else:
            left = pivot + 1
    
    return False

print(binary_search(nums, target))

import heapq

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def trapping_water(height):
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    volume = 0
    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max < right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume


print(trapping_water(height))

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


def dijkstra(graph, start, final):
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

    return costs[final]


print(dijkstra(graph, 1, 8))

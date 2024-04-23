from collections import defaultdict
import heapq


def network_delayed_time(times, n, k):
    graph = defaultdict(list)
    for time in times:
        graph[time[0]].append((time[2], time[1]))

    costs = {}
    pq = []
    heapq.heappush(pq, (0, k))
    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        print(cur_cost, cur_v)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))

    for i in range(1, n + 1):
        if i not in costs:
            return -1
    return max(costs.values())


# times = [[2, 1, 2], [2, 3, 5], [2, 4, 1], [4, 3, 3]]
# n = 4
# k = 2
times = [[1, 2, 1], [2, 1, 3]]
n = 2
k = 2

print(network_delayed_time(times, n, k))

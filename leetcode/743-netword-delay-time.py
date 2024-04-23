import heapq
from collections import defaultdict

times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
# times = [[1, 2, 1]]
# n = 2
# k = 2


def solution(n, k, times):
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
        for i in range(1, end + 1):
            if i not in costs:
                return -1
        return costs[end]

    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((w, v))

    return dijkstra(graph, k, n)


print(solution(n, k, times))

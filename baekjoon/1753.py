# V = 5
# E = 6
# start = 1
# l = [[5, 1, 1], [1, 2, 2], [1, 3, 3], [2, 3, 4], [2, 4, 5], [3, 4, 6]]

import heapq

V, E = map(int, input().split())
start = int(input())

l = []
for i in range(E):
    ll = list(map(int, input().split()))
    l.append(ll)


def solution(V, l, start):
    graph = {}
    for i in range(1, V + 1):
        graph[i] = []
    for u, v, w in l:
        graph[u].append((w, v))

    def dijkstra(graph, start):
        costs = {}
        pq = []
        heapq.heappush(pq, (0, start))

        while pq:
            cur_cost, cur_v = heapq.heappop(pq)
            if cur_v not in costs and cur_v in graph:
                costs[cur_v] = cur_cost
                for cost, next_v in graph[cur_v]:
                    next_cost = cost + cur_cost
                    heapq.heappush(pq, (next_cost, next_v))

        return costs

    costs = dijkstra(graph, start)
    for i in range(1, V + 1):
        if i not in costs:
            print("INF")
        else:
            print(costs[i])

    return


solution(V, l, start)

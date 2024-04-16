import heapq
import sys

input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())

l = []
graph = {}
for i in range(1, V + 1):
    graph[i] = []
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


def dijkstra(graph, start):
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

    return costs


costs = dijkstra(graph, start)

for i in range(1, V + 1):
    try:
        print(costs[i])
    except:
        print("INF")

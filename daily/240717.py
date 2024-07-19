from collections import deque
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

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(3))

def bracket(s):
    q = deque()

    for x in s:
        if x == "(":
            q.append(")")
        elif x == "{":
            q.append("}")
        elif x == "[":
            q.append("]")
        else:
            if not q or x != q.pop():
                return False
    if q:
        return False
    return True

print(bracket("()()[)"))
print(bracket("()()()"))
print(bracket("([)]}"))
print(bracket("{()[]}"))

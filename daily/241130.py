input = 20

def find_prime_list_under_number(number):
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    ans = []
    for i in range(2, number + 1):
        if is_prime(i):
            ans.append(i)

    return ans


result = find_prime_list_under_number(input)
print(result)

input = "01110"


# def find_count_to_turn_out_to_all_zero_or_all_one(string):
#     stack = list(string)
#     if not stack:
#         return 0

#     counter = [0, 0]
#     cur, prev = None, None
#     while stack:
#         cur = stack.pop()

#         if cur == prev:
#             prev = cur
#         else:
#             counter[int(cur)] += 1
#             prev = cur
#     return min(counter)

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    counter = [0, 0]
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i+1] == '0':
                counter[0] += 1
            else:
                counter[1] += 1
    return min(counter)



result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

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

def dijkstra(graph, start, final):
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

    return costs[final]

print(dijkstra(graph, 1, 8))
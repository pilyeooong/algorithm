# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

tickets = [
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
]
# graph = {'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}


# def solution(tickets):
#     dic = {}
#     for ticket in tickets:
#         if ticket[0] not in dic:
#             dic[ticket[0]] = [ticket[1]]
#         else:
#             dic[ticket[0]].append(ticket[1])
#             dic[ticket[0]].sort()


# print(solution(tickets))

from collections import defaultdict


def solution2(tickets):
    graph = defaultdict(list)

    for a, b in sorted(tickets, key=lambda x: x[1]):
        graph[a].append(b)

    route = []

    def dfs(start):
        while graph[start]:
            dfs(graph[start].pop(0))
        route.append(start)

    dfs("ICN")
    return route[::-1]


solution2(tickets)

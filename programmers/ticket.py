from collections import defaultdict

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

tickets = [
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
]
# graph = {'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}


def solution(tickets):
    dic = defaultdict(list)
    for ticket in tickets:
        dic[ticket[0]].append(ticket[1])
    for i in dic:
        dic[i].sort()
    visited = []

    def dfs(ticket):
        while dic[ticket]:
            dfs(dic[ticket].pop(0))
        visited.append(ticket)

    dfs("ICN")

    return visited[::-1]


print(solution(tickets))

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

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

tree_bfs_visited = []
tree_dfs_visited = []

def tree_bfs(root):
    q = deque()
    q.append(root)

    while q:
        cur_node = q.popleft()
        tree_bfs_visited.append(cur_node.value)
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)

    return tree_bfs_visited

print(tree_bfs(root))

def tree_dfs(root):
    if root is None:
        return

    tree_dfs_visited.append(root.value)
    tree_dfs(root.left)
    tree_dfs(root.right)

    return tree_dfs_visited

print(tree_dfs(root))

graph = {
    "A": ["B", "D", "E"],
    "B": ["A", "C", "D"],
    "C": ["B"],
    "D": ["A", "B"],
    "E": ["A"],
}

graph_bfs_visited = []
graph_dfs_visited = []

def graph_bfs(v):
    q = deque()
    q.append(v)
    graph_bfs_visited.append(v)

    while q:
        cur_v = q.popleft()
        for x in graph[cur_v]:
            if x not in graph_bfs_visited:
                q.append(x)
                graph_bfs_visited.append(x)
    return graph_bfs_visited
            
print(graph_bfs('A'))

def graph_dfs(v):
    if v not in graph_dfs_visited:
        graph_dfs_visited.append(v)
    
    for x in graph[v]:
        if x not in graph_dfs_visited:
            graph_dfs(x)
    
    return graph_dfs_visited

print(graph_dfs('A'))

def quick_sort(l, start, end):
    if start >= end:
        return 
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and l[left] <= l[pivot]:
            left += 1
        while right > start and l[right] >= l[pivot]:
            right -= 1
    
        if left > right:
            l[pivot], l[right] = l[right], l[pivot]
        else:
            l[left], l[right] = l[right], l[left]
    
    quick_sort(l, start, right-1)
    quick_sort(l, right+1, end)
    
    return l

arr = [1,3,5,7,2,4,6]

print(quick_sort(arr[:], 0, len(arr) -1))
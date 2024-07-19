import heapq
from collections import deque

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


print(dijkstra(graph, 1, 8)) # 11

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def selection_sort(l):
    for i in range(len(l)):
        min_idx = i
        for j in range(i, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
        l[min_idx], l[i] = l[i], l[min_idx]

    return l

print(selection_sort(array[:]))

def insertion_sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j-1] > l[j]:
                l[j], l[j-1] = l[j-1],l[j]
            else:
                break
    return l

print(selection_sort(array[:]))

def quick_sort(l, start, end):
    if start >= end:
        return
    
    pivot = start
    left =  start + 1
    right = end

    while left <= right:
        if left <= end and l[left] <= l[pivot]:
            left += 1
        if right > start and l[right] >= l[pivot]:
            right -= 1
        
        if left > right:
            l[pivot], l[right] = l[right], l[pivot]
        else:
            l[left], l[right] = l[right], l[left]
    
    quick_sort(l, start, right - 1)
    quick_sort(l, right + 1, end)

    return l

print(quick_sort(array[:], 0, len(array) - 1))
print(array)

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

def tree_bfs(root):
    q = deque()
    q.append(root)

    visited = []

    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

print(tree_bfs(root))

dfs_visited = []
def tree_dfs(root):
    if root is None:
        return
    
    dfs_visited.append(root.value)
    tree_dfs(root.left)
    tree_dfs(root.right)

    return dfs_visited

print(tree_dfs(root))

# grid = [
#     [1, 1, 1, 1, 0],
#     [1, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0],
#     [1, 1, 0, 1, 1]]
grid = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1]]

def islands(grid):
    count = 0
    row = len(grid)
    col = len(grid[0])

    visited = [[False] * col for _ in range(row)]

    def visit(x, y):
        q = deque()
        q.append((x,y))

        deltas = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while q:
            cur_x, cur_y = q.popleft()
            visited[cur_x][cur_y] = True
            
            for dx,dy in deltas:
                next_x, next_y = cur_x + dx, cur_y + dy
                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col and visited[next_x][next_y] == False and grid[next_x][next_y] == 1:
                    q.append((next_x, next_y))
    
    for x in range(row):
        for y in range(col):
            if visited[x][y] == False and grid[x][y] == 1:
                visit(x,y)
                count += 1
    
    return count

print(islands(grid))

graph = {
    "A": ["B", "D", "E"],
    "B": ["A", "C", "D"],
    "C": ["B"],
    "D": ["A", "B"],
    "E": ["A"],
}

def graph_bfs(v):
    visited = []

    q = deque()
    q.append(v)
    visited.append(v)

    while q:
        cur_v = q.popleft()
        for x in graph[cur_v]:
            if x not in visited:
                q.append(x)
                visited.append(x)
    return visited

print(graph_bfs('A'))

graph_dfs_visited = []
def graph_dfs(v):
    if v not in graph_dfs_visited:
        graph_dfs_visited.append(v)
    for x in graph[v]:
        if x not in graph_dfs_visited:
            graph_dfs(x)
    return graph_dfs_visited

print(graph_dfs('A'))

path = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]

def shortest_path(path):
    row = len(path)
    col = len(path[0])

    visited = [[False] * col for _ in range(row)]

    def bfs(x, y, l):
        q = deque()
        q.append((x,y,l))

        deltas = [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]

        while q:
            cur_x, cur_y, cur_l = q.popleft()
            print(cur_x, cur_y)
            if cur_x == row - 1 and cur_y == col - 1:
                return cur_l
            for dx, dy in deltas:
                next_x, next_y, next_l = cur_x + dx, cur_y + dy, cur_l + 1
                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col and path[next_x][next_y] == 0 and visited[next_x][next_y] == False:
                    visited[next_x][next_y] = True
                    q.append((next_x, next_y, next_l))

        return -1

    
    ans = bfs(0,0,1)

    return ans

print(shortest_path(path))

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
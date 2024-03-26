import heapq
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(l):
    head = None
    cur = None
    for x in l:
        node = ListNode(x)
        if head is None:
            head = node
            cur = node
        else:
            cur.next = node
            cur = node
    return head


l = [1, 2, 3, 4, 5, 6]
ll = list_to_linked_list(l)


def swap_node_in_pairs(head):
    root = prev = ListNode(None)

    prev.next = head

    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head

        prev.next = b

        prev = prev.next.next
        head = head.next

    return root.next


result = swap_node_in_pairs(ll)
head = result
while head:
    print(head.val)
    head = head.next


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
    visited = []

    q.append(root)

    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited


tree_dfs_visited = []


def tree_dfs(root):
    if root is None:
        return None

    tree_dfs_visited.append(root.value)
    tree_dfs(root.left)
    tree_dfs(root.right)

    return tree_dfs_visited


print(tree_bfs(root))
print(tree_dfs(root))


graph = {
    "A": ["B", "D", "E"],
    "B": ["A", "C", "D"],
    "C": ["B"],
    "D": ["A", "B"],
    "E": ["A"],
}

graph_dfs_visited = []


def graph_bfs(v):
    q = deque()
    q.append(v)
    visited = [v]

    while q:
        cur_v = q.popleft()
        for x in graph[cur_v]:
            if x not in visited:
                q.append(x)
                visited.append(x)

    return visited


graph_dfs_visited = []


def graph_dfs(v):
    graph_dfs_visited.append(v)

    for x in graph[v]:
        if x not in graph_dfs_visited:
            graph_dfs(x)
    return graph_dfs_visited


print(graph_bfs("A"))
print(graph_dfs("A"))


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def trapping_water(height):
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    volume = 0
    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume


print(trapping_water(height))

grid = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 1, 0], [0, 0, 0, 1, 1]]


def number_of_islands(grid):
    row = len(grid)
    col = len(grid[0])

    visited = [[False] * col for _ in range(row)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    count = 0

    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q:
            cur_x, cur_y = q.popleft()
            for dx, dy in delta:
                next_x, next_y = cur_x + dx, cur_y + dy
                if (
                    next_x >= 0
                    and next_x < row
                    and next_y >= 0
                    and next_y < col
                    and visited[next_x][next_y] == False
                    and grid[next_x][next_y] == 1
                ):
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = True

    for i in range(row):
        for j in range(col):
            if visited[i][j] == False and grid[i][j] == 1:
                bfs(i, j)
                count += 1

    return count


print(number_of_islands(grid))

grid = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 1],
]


def shorted_path(grid):
    row = len(grid)
    col = len(grid[0])

    visited = [[False] * col for _ in range(row)]

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    q = deque()
    q.append((0, 0, 1))

    while q:
        cur_x, cur_y, cur_l = q.popleft()
        if cur_x == row - 1 and cur_y == col - 1:
            return cur_l

        for dx, dy in delta:
            next_x, next_y, next_l = cur_x + dx, cur_y + dy, cur_l + 1
            if (
                next_x >= 0
                and next_x < row
                and next_y >= 0
                and next_y < col
                and grid[next_x][next_y] == 0
                and visited[next_x][next_y] == False
            ):
                q.append((next_x, next_y, next_l))
                visited[next_x][next_y] = True

    return -1


print(shorted_path(grid))

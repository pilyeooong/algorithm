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

        head = head.next
        prev = prev.next.next

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
    visited = []

    q = deque()
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


def graph_dfs(v):
    graph_dfs_visited.append(v)
    for x in graph[v]:
        if x not in graph_dfs_visited:
            graph_dfs(x)
    return graph_dfs_visited


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


print(graph_dfs("E"))
print(graph_bfs("A"))

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def trapping_rain_water(height):
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    volume = 0
    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume


print(trapping_rain_water(height))

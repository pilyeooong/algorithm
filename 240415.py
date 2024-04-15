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
                next_cost = cost + cur_cost
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


print(tree_bfs(root))

tree_dfs_visited = []


def tree_dfs(root):
    if root is None:
        return None

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


def graph_bfs(v):
    visited = []
    q = deque()
    q.append(v)
    visited.append(v)

    while q:
        cur_v = q.popleft()

        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                q.append(v)
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

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

    return array


sorted_array = quick_sort(array, 0, len(array) - 1)
print(sorted_array)


def pythonic_quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return pythonic_quick_sort(left_side) + [pivot] + pythonic_quick_sort(right_side)


sorted_array = pythonic_quick_sort(array)
print(sorted_array)
array.sort()

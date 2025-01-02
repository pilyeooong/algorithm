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

def dijikstra(graph, start, end):
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

print(dijikstra(graph, 1,8))

nums = [1,2,3,4,5,6,7,8,9,10]
target = 2
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return True
        if nums[pivot] > target:
            right = pivot - 1
        else:
            left = pivot + 1
    return False
    # return target in nums

print(binary_search(nums, target))

arr = [1,3,5,2,7,8,4,6,10,9]


# 피봇을 설정하고 오른쪽으로부터는 피봇보다 작은걸 찾고, 왼쪽에서부턴 큰 수를 찾는다. 그리고 해당 숫자끼리 위치를 변경
# left > right 조건에 도달하는 경우 피봇과 작은 값의 위치를 변경. 작은 값의 경우는 right로 부터 찾고 있었으니 right임
# 이후 피봇 이전, 이후의 값을 동일하게 재귀로 정렬 로직 실행
def quick_sort(l, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    if left <= right:
        while left <= end and l[left] <= l[pivot]:
            left += 1
        while right > start and l[right] >= l[pivot]:
            right -= 1
        
        if left > right:
            l[pivot], l[right] = l[right], l[pivot]
        else:
            l[left], l[right] = l[right], l[left]

    quick_sort(l, start, right - 1)
    quick_sort(l, right + 1, end)

    return l

print(quick_sort(arr[:], 0, len(arr) - 1))

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
        cur = q.popleft()
        visited.append(cur.value)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
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
                q.append(v)
                visited.append(v)

    return visited


graph_dfs_visited = []


def graph_dfs(cur_v):
    graph_dfs_visited.append(cur_v)
    
    for v in graph[cur_v]:
        if v not in graph_dfs_visited:
            graph_dfs(v)

    return graph_dfs_visited

print(graph_bfs("A"))
print(graph_dfs("A"))

# def pythonic_quick_sort(array):
#     if len(array) <= 1:
#         return array
    
#     pivot = array[0]
#     tail = array[1:]

#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x > pivot]

#     return pythonic_quick_sort(left_side) + [pivot] + pythonic_quick_sort(right_side)

def pythonic_quick_sort(l):
    if len(l) <= 1:
        return l
    pivot = l[0]
    tail = l[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return pythonic_quick_sort(left) + [pivot] + pythonic_quick_sort(right)

print(pythonic_quick_sort(arr[:]))
import heapq

heap = [5, 2, 1, 3]

heapq.heapify(heap)  # min heap (부모노드가 자식노드보다 값이 작음)
heapq.heappop(heap)  # 우선순위가 높은 노드 추출 dequeue
heapq.heappush(heap, 1)  # enqueue, 우선순위에 맞게 sift up, down에 과정이 있음

heapq._heapify_max(heap)
heapq._heappop_max(heap)  # 5

max_heap = [5, 2, 9, 1, 2, 3]
max_heap = [-1 * x for x in max_heap]
heapq.heapify(max_heap)
weight = heapq.heappop(max_heap)
value = -1 * weight  # 9

max_heap = [5, 2, 9, 1, 2, 3]
max_heap = [(-1 * x, x) for x in max_heap]
heapq.heapify(max_heap)
weight, value = heapq.heappop(max_heap)
print(weight, value)

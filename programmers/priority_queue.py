import heapq

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]


def solution(operations):
    answer = [0, 0]
    l = []
    for operation in operations:
        l.append(list(operation.split()))
    pq = []

    for x in l:
        if x[0] == "I":
            heapq.heappush(pq, int(x[1]))
        elif x[0] == "D":
            if pq:
                if x[1] == "-1":
                    heapq.heappop(pq)
                else:
                    for i in range(len(pq)):
                        pq[i] = -1 * pq[i]
                    heapq.heapify(pq)
                    heapq.heappop(pq)
                    for i in range(len(pq)):
                        pq[i] = -1 * pq[i]
                    heapq.heapify(pq)

    if pq:
        answer = [max(pq), min(pq)]
    return answer


print(solution(operations))
# solution(operations)

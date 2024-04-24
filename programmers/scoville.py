import heapq

scoville = [1, 2]
K = 7


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        if scoville[0] >= K:
            break
        if len(scoville) >= 2:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            total = first + (second * 2)
            heapq.heappush(scoville, total)
            answer += 1
        else:
            answer = -1
            break

    return answer


print(solution(scoville, K))

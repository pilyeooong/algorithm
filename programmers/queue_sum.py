from collections import deque


def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    deque1 = deque(queue1)
    deque2 = deque(queue2)

    answer = -1
    for i in range(4 * len(queue1) + 1):
        if sum1 == sum2:
            answer = i
            break

        if sum1 > sum2:
            x = deque1.popleft()
            deque2.append(x)
            sum2 += x
            sum1 -= x
        else:
            x = deque2.popleft()
            deque1.append(x)
            sum1 += x
            sum2 -= x

    return answer


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

print(solution(queue1, queue2))

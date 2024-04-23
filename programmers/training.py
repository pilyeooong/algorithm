def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    for i in range(1, n + 1):
        if i in reserve and i in lost:
            reserve.pop(reserve.index(i))
            answer += 1
            continue
        if i in lost:
            if i - 1 in reserve:
                reserve.pop(reserve.index(i - 1))
                answer += 1
                continue
            if i + 1 in reserve:
                reserve.pop(reserve.index(i + 1))
                answer += 1
                continue
        else:
            answer += 1
    return answer


n = 5
lost = [3, 4]
reserve = [4, 3]

print(solution(n, lost, reserve))

# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2

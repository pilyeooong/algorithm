def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0 or answer[-1] != i:
            answer.append(i)
    return answer


arr = [1, 1, 3, 3, 0, 1, 1]

print(solution(arr))

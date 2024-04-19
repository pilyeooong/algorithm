numbers = [1, 1, 1, 1, 1]
target = 3

# numbers = [4, 1, 2, 1]
# target = 4


def solution(numbers, target):
    answer = 0

    def dfs(i, result):
        if i == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(i + 1, result + numbers[i])
            dfs(i + 1, result - numbers[i])

    dfs(0, 0)

    return answer


print(solution(numbers, target))

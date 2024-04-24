def solution(number, k):
    answer = ""

    stack = []

    for num in number:
        if stack and k > 0:
            while stack and stack[-1] < num and k > 0:
                stack.pop()
                k -= 1

        stack.append(num)

    answer = "".join(stack)
    if k > 0:
        answer = answer[:-k]
    return answer


# number = "1924"
# k = 2
# number = "1231234"
# k = 3
number = "4177252841"
k = 4

print(solution(number, k))

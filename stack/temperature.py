def solution(temperatures):
    ans = [0] * len(temperatures)
    stack = []
    for day, temperature in enumerate(temperatures):
        while stack and stack[-1][1] < temperature:
            prev = stack.pop()
            ans[prev[0]] = day - prev[0]
        stack.append([day, temperature])
    return ans


# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
temperatures = [73, 71, 69, 67, 72, 76]
ans = solution(temperatures)
print(ans)

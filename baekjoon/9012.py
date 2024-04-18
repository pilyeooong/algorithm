def solution(s):
    stack = []

    for c in s:
        if c == "(":
            stack.append(")")
        elif c == "[":
            stack.append("]")
        elif c == "{":
            stack.append("}")
        elif not stack or stack.pop() != c:
            print("NO")
            return
    if stack:
        print("NO")
    else:
        print("YES")


T = int(input())
for _ in range(T):
    s = input()
    solution(s)

# s = "(())())"
# s = "(((()())()"
# s = "(()())((()))"

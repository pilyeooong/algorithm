def solution(str):
    bracket_list = [s for s in str]
    small_brackets = ["(", ")"]
    medium_brackets = ["{", "}"]
    large_brackets = ["[", "]"]
    open_brackets = ["(", "{", "["]

    stack = []
    for bracket in bracket_list:
        if bracket in open_brackets:
            stack.append(bracket)
        else:
            if bracket in small_brackets:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            if bracket in medium_brackets:
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            if bracket in large_brackets:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
    if len(stack) > 0:
        return False
    return True


# result = solution("()()()")
# print(result)

# result = solution("([)]}")
# print(result)

# result = solution("{()[]}")
# print(result)


def solution2(str):
    stack = []
    for s in str:
        if s == "(":
            stack.append(")")
        elif s == "{":
            stack.append("}")
        elif s == "[":
            stack.append("]")
        elif not stack or stack.pop() != s:
            return False
    return not stack


# result = solution2("()()()")
# print(result)

# result = solution2("([)]}")
# print(result)

# result = solution2("{()[]}")
# print(result)


def solution3(str):
    stack = []
    for s in str:
        if s == "(":
            stack.append(")")
        elif s == "{":
            stack.append("}")
        elif s == "[":
            stack.append("]")
        elif not stack or stack.pop() != s:
            return False

    return not stack


result = solution3("()()()")
print(result)

result = solution3("([)]}")
print(result)

result = solution3("{()[]}")
print(result)

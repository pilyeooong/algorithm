from collections import deque

s = ")()("


def solution(s):
    q = deque()

    for c in s:
        if c == "(":
            q.append(")")
        elif not q or q.pop() != c:
            return False
    if q:
        return False

    return True


print(solution(s))

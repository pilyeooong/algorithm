from collections import deque


# def solution(s):
#     checker = []
#     for l in s:
#         if l.isalnum():
#             checker.append(l.lower())
#     reverse = checker[::-1]

#     return checker == reverse


def solution(s):
    q = deque()
    for l in s:
        if l.isalnum():
            q.append(l.lower())

    while q and len(q) > 1:
        first, last = q.popleft(), q.pop()

        if first != last:
            return False
    return True


# s = "race a car"
s = "A man, a plan, a canal: Panama"
print(solution(s))

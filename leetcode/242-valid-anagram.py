# s, t = "anagram", "nagaram"
s, t = "rat", "car"


def solution(s, t):
    if sorted(s) != sorted(t):
        return False

    return True


print(solution(s, t))

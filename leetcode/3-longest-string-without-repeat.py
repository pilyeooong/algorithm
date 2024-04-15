s = "pwwkew"
# abc = 3


def solution(s):
    result = ""
    for i in range(len(s)):
        temp = s[i]
        for j in range(i + 1, len(s)):
            if s[j] in temp:
                break
            else:
                temp += s[j]
        result = max(result, temp, key=len)

    print(result)

    return len(result)


print(solution(s))

s = "02984"

27 * 8 * 4


def solution(s):
    ans = int(s[0])
    for i in range(1, len(s)):
        if i - 1 >= 0 and s[i - 1] == "1" or s[i - 1] == "0":
            ans += int(s[i])
        else:
            ans *= int(s[i])
        print(ans)

    return ans


def solution(s):
    ans = int(s[0])
    for i in range(1, len(s)):
        num = int(s[i])
        if num <= 1 or ans <= 1:
            ans += num
        else:
            ans *= num

    return ans


print(solution(s))

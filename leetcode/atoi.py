def solution(s):
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648

    ans = 0

    sign = 1

    check = ''
    strip_s = s.strip()

    for i in range(len(strip_s)):
        if i == 0 and (strip_s[i] == '-' or strip_s[i] == '+'):
            sign = -1 if strip_s[i] == '-' else 1
        elif strip_s[i].isdigit():
            check += strip_s[i]
        else:
            break
    
    if check:
        ans = int(check) * sign
    if ans > INT_MAX:
        return INT_MAX
    if ans < INT_MIN:
        return INT_MIN

    return ans

print(solution('-+12'))
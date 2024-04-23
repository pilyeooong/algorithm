def solution(s, find_s):
    ans = 0

    len_find_s = len(find_s)

    while s:
        find_index = s.find(find_s)
        if find_index != -1:
            s = s[find_index + len_find_s :]
            ans += 1
        else:
            break
    return ans


s = input()
find_s = input()
print(solution(s, find_s))

s = "AJKDLSI412K4JSJ9D"


def solution(s):
    strs = []
    nums = []
    for c in s:
        if c.isalpha():
            strs.append(c)
        else:
            nums.append(c)
    strs.sort()
    sum_nums = sum(map(int, nums))

    return "".join(strs) + str(sum_nums)


print(solution(s))

num1 = [1, 2]
num2 = [3, 4]


def solution(num1, num2):
    l = sorted(num1 + num2)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2] + l[(len(l) // 2 - 1)]) / 2


print(solution(num1, num2))

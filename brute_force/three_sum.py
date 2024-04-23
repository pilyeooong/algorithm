l = [4, 9, 7, 5, 1]
target = 15


def solution(l, target):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == target:
                    print(l[i], l[j], l[k])
                    return True
    return False


print(solution(l, target))

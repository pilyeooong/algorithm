def solution(number, k):
    answer = ""

    l = list(number)
    for _ in range(k):
        minimum = min(l)
        rm = l.index(minimum)
        l.pop(rm)

    return answer.join(l)


# number = "1924"
# k = 2
# number = "1231234"
# k = 3
number = "4177252841"
k = 4

print(solution(number, k))

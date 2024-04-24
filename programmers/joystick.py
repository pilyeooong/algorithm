name = "JAN"


def solution(name):
    init = ["A"] * len(name)

    ord_init = [ord(x) for x in init]
    ord_name = [ord(x) for x in name]
    min_move = len(name) - 1

    l = []
    for i in range(len(ord_init)):
        from_z = 90 - ord_name[i] + 1
        from_a = ord_name[i] - ord_init[i]

        if from_z < from_a:
            l.append(from_z)
        else:
            l.append(from_a)

        # ref
        # https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy#%EC%B6%94%EA%B0%80-%EC%84%A4%EB%AA%85
        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    return sum(l) + min_move


print(solution(name))

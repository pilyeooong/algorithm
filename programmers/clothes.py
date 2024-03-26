from collections import defaultdict

clothes = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
]


def solution(clothes):
    answer = 1
    hash = defaultdict(list)
    for cloth, kind in clothes:
        hash[kind].append(cloth)

    for i in hash.keys():
        print(len(hash[i]) + 1)
        answer *= len(hash[i]) + 1

    answer -= 1
    return answer


print(solution(clothes))

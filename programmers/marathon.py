from collections import defaultdict

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]


def solution(participant, completion):
    answer = ""
    dic = defaultdict(int)

    for p in participant:
        dic[p] += 1

    for c in completion:
        dic[c] -= 1

    for k, v in dic.items():
        if v >= 1:
            return k

    return answer


print(solution(participant, completion))

from collections import defaultdict


def solution(answers):
    l = [
        [1, 2, 3, 4, 5],
        [
            2,
            1,
            2,
            3,
            2,
            4,
            2,
            5,
        ],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]
    scores = [0, 0, 0]

    for idx, answer in enumerate(answers):
        if answer == l[0][idx % len(l[0])]:
            scores[0] += 1
        if answer == l[1][idx % len(l[1])]:
            scores[1] += 1
        if answer == l[2][idx % len(l[2])]:
            scores[2] += 1

    ans = []
    max_score = max(scores)
    for idx, score in enumerate(scores):
        if score == max_score:
            ans.append(idx + 1)
    ans.sort()
    return ans


answers = [1, 2, 3, 4, 5]
print(solution(answers))

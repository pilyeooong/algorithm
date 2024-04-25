from collections import defaultdict


# 높은 점수를 받은 학생 반환 ex) [1]
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
        for i in range(len(l)):
            if answer == l[i][idx % len(l[i])]:
                scores[i] += 1
    ans = []
    max_score = max(scores)
    for idx, score in enumerate(scores):
        if score == max_score:
            ans.append(idx + 1)
    ans.sort()
    return ans


answers = [1, 2, 3, 4, 5]
print(solution(answers))

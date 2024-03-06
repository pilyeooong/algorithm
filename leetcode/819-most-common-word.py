import re
from collections import Counter
from collections import defaultdict

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


def solution(paragraph, banned):
    s = re.sub(r"[^\w]", " ", paragraph).lower().split()
    words = [word for word in s if word not in banned]

    # counter = Counter(words)
    # return counter.most_common()[0][0]

    counter = defaultdict(int)

    for word in words:
        counter[word] += 1
    return max(counter, key=counter.get)


print(solution(paragraph, banned))

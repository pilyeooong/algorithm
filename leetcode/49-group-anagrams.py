from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


def solution(strs):
    anagrams = defaultdict(list)
    for word in strs:
        anagrams["".join(sorted(word))].append(word)
    return anagrams.values()


print(solution(strs))

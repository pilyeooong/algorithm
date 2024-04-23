import sys

input = sys.stdin.readline


n = int(input())
words = []
for _ in range(n):
    words.append(input())


def solution(words):
    sorted_words = sorted(words, key=lambda x: (len(x), x))
    unique_words = []
    [unique_words.append(x) for x in sorted_words if x not in unique_words]
    return unique_words


answer = solution(words)
for word in answer:
    print(word, end="")

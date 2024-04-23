import sys

input = sys.stdin.readline


def solution(words):
    def is_group_word(word):
        checker = []
        for i in range(len(word)):
            if word[i] in checker:
                if i - 1 >= 0 and word[i - 1] != word[i]:
                    return False
            else:
                checker.append(word[i])

        return True

    answer = 0
    for word in words:
        if is_group_word(word) == True:
            answer += 1

    return answer


n = int(input())
words = []
for _ in range(n):
    words.append(input())
print(solution(words))

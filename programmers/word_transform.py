from collections import deque


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    if begin == target:
        return answer

    def similar(a, b):
        score = 0
        for x, y in zip(a, b):
            if x != y:
                score += 1
        if score > 1:
            return False
        return True

    def bfs(begin):
        q = deque()
        q.append((begin, 0))

        while q:
            cur_word, cur_count = q.popleft()
            if cur_word == target:
                return cur_count
            for word in words:
                if similar(cur_word, word):
                    q.append((word, cur_count + 1))

    answer = bfs(begin)

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))

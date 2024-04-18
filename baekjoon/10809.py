s = "baekjoon"


s = input()


def solution(s):
    start = ord("a")
    end = ord("z") + 1
    l = list(map(ord, s))

    for i in range(start, end):
        if i in l:
            print(l.index(i), end=" ")
        else:
            print(-1, end=" ")


solution(s)

def solution(l):
    R = l[0]
    S = l[1]

    l = list(S)

    for x in l:
        for _ in range(int(R)):
            print(x, end="")
    print("")


T = int(input())
l = []
for _ in range(T):
    R, S = map(str, input().split())
    l.append([R, S])
for i in l:
    solution(i)

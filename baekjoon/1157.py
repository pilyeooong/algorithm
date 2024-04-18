s = "baaa"

s = input()


def solution(s):
    lower_s = s.lower()
    count = {}

    for c in lower_s:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    print(count.get())

    values = count.values()
    maximum = max(values)
    t = sum([1 for x in values if x >= maximum])

    if t > 1:
        print("?")
    else:
        print(max(count, key=count.get).upper())


solution(s)

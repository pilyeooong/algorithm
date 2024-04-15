l = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j - 1], l[j] = l[j], l[j - 1]
            else:
                break
    return l


print(sort(l))


for i in range(1, 0, -1):
    print(i)

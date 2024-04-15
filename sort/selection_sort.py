l = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]


def sort(l):

    for i in range(len(l)):
        minimum_index = i
        for j in range(i + 1, len(l)):
            if l[minimum_index] > l[j]:
                minimum_index = j
        l[i], l[minimum_index] = l[minimum_index], l[i]
    return l


print(sort(l))

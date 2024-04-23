l = [(1, 3), (2, 1), (1, 2), (2, 3)]

l.sort(key=lambda x: (x[1], x[0]))
print(l)
# 21 12 13 23

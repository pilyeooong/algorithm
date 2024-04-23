n = input()

l = list(n)

sorted_l = sorted(list(map(int, l)), reverse=True)

print("".join(list(map(str, sorted_l))))

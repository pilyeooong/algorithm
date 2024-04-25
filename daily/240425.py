from itertools import permutations

s = "011"

list_s = list(s)
nums = []

for i in range(len(list_s)):
    permutation_set = set(list(permutations(list_s, i + 1)))
    for i in permutation_set:
        print(i)
        print("".join(i))

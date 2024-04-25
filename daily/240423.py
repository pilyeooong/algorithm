from itertools import combinations

nums = [1, 2, 3, 4]

print(list(combinations(nums, 2)))

l = [[1, 2, 3], [4, 5, 6]]


print([element for sub_list in l for element in sub_list])

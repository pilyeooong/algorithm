s = "day1compn" # 0
s = "aabb" # -1
s = "abacdb" # 2
s = "aabbaccdb" # 3

def find_unique_string(string):
    check = {}
    for s in string:
        if s not in check:
            check[s] = 1
        else:
            check[s] += 1
    set_values = set(check.values())

    if len(set_values) == 1 and list(set_values)[0] == 1:
        return 0
    elif len(set_values) == 1 and list(set_values)[0] != 1:
        return -1
    else:
        return sum(1 for x in check.values() if x > 1)

result = find_unique_string(s)
print(result)


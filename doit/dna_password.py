# 백준 12891

# A, C, G, T
# S, P = map(int, input().split())
# dna_str_list = list(input())
# dna_str_count_list = list(map(int, input().split()))
# cnt = 0


# dic = {"A": 0, "C": 0, "G": 0, "T": 0}
# checker = {
#     "A": dna_str_count_list[0],
#     "C": dna_str_count_list[1],
#     "G": dna_str_count_list[2],
#     "T": dna_str_count_list[3],
# }


# def valid(dic):
#     for k in dic:
#         if dic[k] < checker[k]:
#             return False
#     return True


# for i in range(P):
#     dic[dna_str_list[i]] += 1
# is_valid = valid(dic)
# if is_valid:
#     cnt += 1

# for i in range(P, S):
#     j = i - P
#     dic[dna_str_list[i]] += 1
#     dic[dna_str_list[j]] -= 1
#     is_valid = valid(dic)
#     if is_valid:
#         cnt += 1

# print(cnt)

# -------------------

# A, C, G, T
S, P = map(int, input().split())
dna_str_list = list(input())
dna_str_count_list = list(map(int, input().split()))
cnt = 0


dic = {"A": 0, "C": 0, "G": 0, "T": 0}
checker = {
    "A": dna_str_count_list[0],
    "C": dna_str_count_list[1],
    "G": dna_str_count_list[2],
    "T": dna_str_count_list[3],
}

for i in range(S - P + 1):
    flag = True
    if i == 0:
        for j in range(P):
            dic[dna_str_list[j]] += 1
    else:
        dic[dna_str_list[i - 1]] -= 1
        dic[dna_str_list[i + P - 1]] += 1

    for k in dic:
        if dic[k] < checker[k]:
            flag = False
    if flag:
        cnt += 1

print(cnt)

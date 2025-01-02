# def find_max_num(array):
#     return max(array)

def find_max_num(array):
    max_num = array[0]
    for i in range(1, len(array)):
        if array[i] > max_num:
            max_num = array[i]

    return max_num


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))

# def find_max_occurred_alphabet(string):
#     checker = {}

#     for s in string:
#         if not s.isalpha():
#             continue 
#         if s not in checker:
#             checker[s] = 1
#         else:
#             checker[s] += 1

#     return max(sorted(checker.keys()), key=lambda x: checker[x])

def find_max_occurred_alphabet(string):
    checker = [0] * 26

    for s in string:
        if s.isalpha():
            checker[ord(s) - 97] += 1
    
    ans = chr(checker.index(max(checker)) + 97)
    return ans


print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))


def find_max_occurred_num(nums):
    ans = -1
    checker = {}
    for num in nums:
        if num not in checker:
            checker[num] = 1
        else:
            checker[num] += 1
    checker_values = list(checker.values())
    max_count = max(checker_values)
    if checker_values.count(max_count) > 1:
        return ans
    for k, v in checker.items():
        if v == max_count:
            ans = k
    return ans

print(find_max_occurred_num([1, 2, 3, 3, 3, 4]))
print(find_max_occurred_num([1, 1, 2, 2]))
print(find_max_occurred_num([1]))
print(find_max_occurred_num([0]))
print(find_max_occurred_num([0,0,1,0]))
print(find_max_occurred_num([11, 1, 1]))
print(find_max_occurred_num([1, 2, 1, 2, 1, 2, 1]))


def find_all_prime_nums(num):
    ans = []
    def check_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    for i in range(2, num+1):
        if check_prime(i) == True:
            ans.append(i)

    return ans

print(find_all_prime_nums(20))


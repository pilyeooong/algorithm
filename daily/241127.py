# def is_number_exist(number, array):
#     for n in array:
#         if n == number:
#             return True
#     return False

def is_number_exist(number, array):
    if number not in array:
        return False
    return True


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = False 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))

def find_max_plus_or_multiply(array):
    total = 0
    for n in array:
        if n <= 1 or total <= 1: # total이 1인 경우까지는 더하는게 더 숫자가 커진다 ex) 1 + 2 < 1 * 2
            total += n
        else:
            total *= n

    return total


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))

input = "abadabac"

def find_not_repeating_first_character(string):
    for s in string:
        if string.count(s) == 1:
            return s
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))

input = 20


def find_prime_list_under_number(number):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    ans = []
    for i in range(2, number):
        if is_prime(i):
            ans.append(i)
    return ans


result = find_prime_list_under_number(input)
print(result)

input = "0001100110000"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    counter = [0, 0]

    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            if string[i] == '0':
                counter[0] += 1
            else:
                counter[1] += 1

    return min(counter)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

# def summarize_string(target_string):
#     # 이 부분을 채워보세요!
#     n = len(target_string)
#     count = 0
#     result_str = ''

#     for i in range(n - 1):
#         if target_string[i] == target_string[i + 1]:
#             count += 1
#         else:
#             result_str += target_string[i] + str(count + 1) + '/'
#             count = 0

#     result_str += target_string[n - 1] + str(count + 1)

#     return result_str

def summarize_string(target_string):
    counter = {}
    for s in target_string:
        if s not in counter:
            counter[s] = 1
        else:
            counter[s] += 1

    ans_string = ""
    for k, v in counter.items():
        if len(ans_string) == 0:
            ans_string += f"{k}{v}"
        else:
            ans_string += f"/{k}{v}"

    return ans_string
input_str = "acccdeee"

print(summarize_string(input_str)) # a1/c3/d1/e3
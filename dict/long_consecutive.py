# 가장 긴 연속된 수의 길이
# ex) [1,2,3,4] = 4
def solution(nums):
    dict = {}
    max_count = 0
    dict = {num: num + 1 for num in nums}
    print(dict)

    for num in nums:
        if num - 1 not in dict:
            count = 1
            find_num = dict[num]
            while find_num in dict:
                find_num = dict[find_num]
                count += 1
            if max_count < count:
                max_count = count

    return max_count


# nums = [100, 4, 200, 1, 3, 2]
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(sorted(nums))
print(solution(nums))

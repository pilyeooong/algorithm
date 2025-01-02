# l = [1,5,7,8,3,2,4,6,10,9]
# def quick_sort(array):
#     if len(array) <= 1:
#         return array

#     pivot = array[0]
#     tail = array[1:]
#     left = [x for x in tail if x <= pivot]
#     right = [x for x in tail if x > pivot]

#     return quick_sort(left) + [pivot] + quick_sort(right)

# def quick_sort2(array, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end

#     if left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
        
#         if left > right:
#             array[pivot], array[right] = array[right], array[pivot]
#         else:
#             array[left], array[right] = array[right], array[left]
        
#     quick_sort2(array, start, right - 1)
#     quick_sort2(array, right + 1, end)

#     return array

# result = quick_sort(l[:])
# print(result)

# result = quick_sort2(l[:], 0, len(l) - 1)
# print(result)

# def binary_search(l, target):
#     l.sort()

#     left = 0
#     right = len(l) - 1

#     while left <= right:
#         pivot = (left + right) // 2
#         if l[pivot] == target:
#             return True
#         if l[pivot] < target:
#             left = pivot + 1
#         else:
#             right = pivot -1

#     return False

# result = binary_search(l[:], 9)
# print(result)

# input = [4, 6, 2, 9, 1]


# def bubble_sort(array):
#     for i in range(len(array)):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j + 1], array[j] = array[j], array[j + 1]
#     return array


# bubble_sort(input)
# print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

# print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ", bubble_sort([4, 6, 2, 9, 1]))
# print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ", bubble_sort([3,-1,17,9]))
# print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ", bubble_sort([100,56,-3,32,44]))

# def selection_sort(array):
#     for i in range(len(array)):
#         minimum_index = i
#         for j in range(i, len(array)):
#             if array[minimum_index] > array[j]:
#                 minimum_index = j
#         array[minimum_index], array[i] = array[i], array[minimum_index]
    
#     return array


# print("----------- selection sort -----------")
# input = [4, 6, 2, 9, 1]
# selection_sort(input)
# print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

# print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
# print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
# print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))

# print("----------- merge sort -----------")

# array_a = [1, 2, 3, 5]
# array_b = [4, 6, 7, 8]

# def merge(array1, array2):
#     index1, index2 = 0, 0

#     res = []

#     while True:
#         if index1 >= len(array1):
#             for x in array2[index2:]:
#                 res.append(x)
#             break
#         if index2 >= len(array2):
#             for x in array1[index1:]:
#                 res.append(x)
#             break
#         if array1[index1] < array2[index2]:
#             res.append(array1[index1])
#             index1 += 1
#         else:
#             res.append(array2[index2])
#             index2 += 1
    
#     return res


# print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

# print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
# print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
# print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))

# array = [5, 3, 2, 1, 6, 8, 7, 4]


# def merge_sort(array):
#     if len(array) <= 1:
#         return array

#     mid = len(array) // 2
#     left = merge_sort(array[0:mid])
#     right = merge_sort(array[mid:])

#     return merge(left, right)

# print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

# print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]))
# print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]))
# print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1, -1, 0, 1, 6, 9, 10]))

top_heights = [6, 9, 5, 7, 4]


# def get_receiver_top_orders(heights):
#     ans = [0] * len(heights)
#     for i in range(len(heights) - 1 , -1, -1):
#         for j in range(i - 1, -1, -1):
#             if heights[i] < heights[j]:
#                 ans[i] = j + 1
#                 break
#     return ans


def get_receiver_top_orders(heights):
    ans = [0] * len(heights)
    while heights:
        height = heights.pop()
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] >= height:
                ans[len(heights)] = i + 1
                break
    return ans


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

# print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
# print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
# print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))
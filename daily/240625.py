def solution(s):
    try:
        int(s)
        l = []
        for i in range(len(s) - 2):
            if s[i] == s[i+1] == s[i+2]:
                l.append(int(s[i]+s[i+1]+s[i+2]))
        if len(l) <= 0:
            return -1
        return max(l)
    except:
        return -1

s = "asd"
print(solution(s))

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left],array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right+ 1, end)

    return array

print(quick_sort(array, 0, len(array)-1))

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[min_idx], array[i] = array[i], array[min_idx]
    return array

selection_sort(array)
print(array)
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def sort(array, start, end):
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
            array[left], array[right] = array[right], array[left]

    sort(array, start, right - 1)
    sort(array, right + 1, end)


print(sort(array, 0, len(array) - 1))

print(array)

# array = [10, 1, 2, 3, 4, 5]
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def pythonic_quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return pythonic_quick_sort(left_side) + [pivot] + pythonic_quick_sort(right_side)


print(pythonic_quick_sort(array))

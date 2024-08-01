def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i), end=", ")
print('...')

arr = [1,3,5,2,7,8,4,6,10,9]

def quick_sort(l, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    if left <= right:
        while left <= end and l[left] <= l[pivot]:
            left += 1
        while right > start and l[right] >= l[pivot]:
            right -= 1
        
        if left > right:
            l[pivot], l[right] = l[right], l[pivot]
        else:
            l[left], l[right] = l[right], l[left]
    
    quick_sort(l, start, right -1)
    quick_sort(l, right + 1, end)

    return l

print(quick_sort(arr[:], 0, len(arr) - 1))
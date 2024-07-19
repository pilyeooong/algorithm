# [1,3,0,1]
arr = [1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    for v in arr:
        if len(answer) == 0 or answer[-1] != v:
            answer.append(v)

    return answer

print(solution(arr))

def stocks(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

prices = [1, 2, 3, 2, 3]
print(stocks(prices))

def quick_sort(l, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if left <= end and l[left] <= l[pivot]:
            left += 1
        if right > start and l[right] >= l[pivot]:
            right -= 1
        
        if left > right:
            l[pivot], l[right] = l[right], l[pivot]
        else:
            l[left], l[right] = l[right], l[left]
    
    quick_sort(l, start, right - 1)
    quick_sort(l, right + 1, end)

    return l

array = [1,5,6,3,2,8,9,4,7]

print(quick_sort(array[:], 0, len(array) - 1))

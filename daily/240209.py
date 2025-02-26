a, b, c = 5, 2, 3

l = [a, b, c]
def quick_sort(l):
    if len(l) <= 1:
        return l

    pivot = l[0]
    tail = l[1:]

    left = [x for x in tail if x < pivot]
    right = [x for x in tail if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

ans = quick_sort(l[:])
print(ans)

def selection_sort(l):
    for i in range(len(l)):
        min_idx = i

        for j in range(i + 1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
        
        l[i], l[min_idx] = l[min_idx], l[i]

    return l

ans = selection_sort(l[:])
print(ans)
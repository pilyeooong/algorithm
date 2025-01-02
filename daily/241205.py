class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


def get_linked_list_sum(linked_list_1, linked_list_2):
    def get_num_from_linked_list(head):
        num = 0
        while head:
            num = num * 10 + head.data
            head = head.next
        return num

    head1 = linked_list_1.head
    head2 = linked_list_2.head

    first_num = get_num_from_linked_list(head1)
    second_num = get_num_from_linked_list(head2)
    
    return first_num + second_num


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))

def bs(target, array):
    left = 0
    right = len(array) - 1

    while left <= right:
        pivot = (left + right) // 2

        if array[pivot] == target:
            return True
        if array[pivot] < target:
            left = pivot + 1
        else:
            right = pivot - 1
    
    return False

target = 3
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
result = bs(target, array)
print(result)

l = [1,5,7,8,3,2,4,6,10,9]
def quick_sort(l):
    if len(l) <= 1:
        return l

    pivot = l[0]
    tail = l[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

def quick_sort2(l, start, end):
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
    
    quick_sort2(l, start, right - 1)
    quick_sort2(l, right + 1, end)

    return l


# result = quick_sort(l[:])
# print(result)

result = quick_sort2(l[:], 0, len(l) - 1)
print(result)
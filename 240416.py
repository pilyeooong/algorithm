array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def selection_sort(l):
    for i in range(len(l)):
        minimum_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[minimum_index]:
                minimum_index = j
        l[minimum_index], l[i] = l[i], l[minimum_index]

    return l


def insertion_sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j - 1], l[j] = l[j], l[j - 1]
            else:
                break
    return l


def quick_sort(l, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and l[left] <= l[pivot]:
            left += 1
        while right > start and l[right] >= l[pivot]:
            right -= 1

        if left > right:
            l[pivot], l[right] = l[right], l[pivot]
        else:
            l[left], l[right] = l[right], l[left]

    quick_sort(l, start, right - 1)
    quick_sort(l, right + 1, end)

    return l


print(selection_sort(array))
print(insertion_sort(array))
print(quick_sort(array, 0, len(array) - 1))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(l):
    head = None
    cur = None
    for x in l:
        node = ListNode(x)
        if head is None:
            head = node
            cur = node
        else:
            cur.next = node
            cur = node
    return head


l = [1, 2, 3, 4, 5, 6]
ll = list_to_linked_list(l)


def swap_node_in_pairs(head):
    root = prev = ListNode(None)

    prev.next = head

    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head

        prev.next = b

        prev = prev.next.next
        head = head.next

    return root.next


result = swap_node_in_pairs(ll)
head = result
while head:
    print(head.val)
    head = head.next

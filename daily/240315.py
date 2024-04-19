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


l = [1, 2, 3, 4]
# [2,1,4,3]
l = [1, 2, 3, 4, 5, 6]
head = list_to_linked_list(l)


def swap_in_pairs(head):
    root = prev = ListNode(None)

    prev.next = head

    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head

        prev.next = b

        head = head.next
        prev = prev.next.next

    return root.next


result = swap_in_pairs(head)
head = result
while head:
    print(head.val)
    head = head.next

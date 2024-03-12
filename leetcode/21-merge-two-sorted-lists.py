class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(l1, l2):
    if not l1 or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = solution(l1.next, l2)
    return l1


l1 = ListNode(1, next=ListNode(2, next=ListNode(4)))
l2 = ListNode(1, next=ListNode(3, next=ListNode(4)))

result = solution(l1, l2)


head = result
while head:
    print(head.val)
    head = head.next


def solution2(l1, l2):
    dummy = ListNode()

    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2

    return dummy.next


result = solution2(l1, l2)
head = result
while head:
    print(head.val)
    head = head.next

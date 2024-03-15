class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(node, prev=None):
    if not node:
        return prev
    next, node.next = node.next, prev
    return solution(next, node)


# 1 2 3 4 5
# 5 4 3 2 1
def solution2(head):
    node, prev = head, None

    while node:
        next = node.next
        node.next = prev

        prev = node
        node = next
    return prev


l1 = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))


result2 = solution2(l1)


head = result2
while head:
    print(head.val)
    head = head.next

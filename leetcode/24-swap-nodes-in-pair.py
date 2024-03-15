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


# 값만 바꾸기
# def solution(head):
#     cur = head
#     while cur and cur.next:
#         cur.val, cur.next.val = cur.next.val, cur.val
#         cur = cur.next.next
#     return head

# b = head.next
# head.next = b.next
# b.next = head

# prev.next = b

# head = head.next
# prev = prev.next.next


def solution2(head):
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


l = [1, 2, 3, 4]
# TODO: 아래 인풋으로 풀어보기
l = [1, 2, 3, 4, 5, 6]
ll = list_to_linked_list(l)
result = solution2(ll)

h = result
while h:
    print(h.val)
    h = h.next

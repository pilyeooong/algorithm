class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(2, next=ListNode(4, next=ListNode(3)))
l2 = ListNode(5, next=ListNode(6, next=ListNode(4)))


def solution(l1, l2):
    def reverse(head):
        node, prev = head, None

        while node:
            next = node.next
            node.next = prev

            prev = node
            node = next
        return prev

    def listToLinkedList(l):
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

    reversed_list = [reverse(l1), reverse(l2)]
    reversed_nums = []
    for reversed in reversed_list:
        nums = []
        head = reversed
        while head:
            nums.append(str(head.val))
            head = head.next
        reversed_nums.append(nums)

    total = 0
    for reversed_num in reversed_nums:
        total += int("".join(reversed_num))

    l_list = listToLinkedList(list(str(total)))
    reversed_l_list = reverse(l_list)

    return reversed_l_list


result = solution(l1, l2)

head = result
while head:
    print(head.val)
    head = head.next

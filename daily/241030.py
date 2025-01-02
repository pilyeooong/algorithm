# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ListNode가 아닌경우
# def addTwoNumbers(l1, l2):
#     l1.reverse()
#     l2.reverse()

#     total = 0
#     reversed_l1 = ""
#     reversed_l2 = ""
#     for num in l1:
#         reversed_l1 += reversed_l1.join(str(num))
#     for num in l2:
#         reversed_l2 += reversed_l2.join(str(num))
    
    
#     total = int(reversed_l1) + int(reversed_l2)

#     ans = list(map(int, list(str(total))))
#     ans.reverse()

#     return ans

def addTwoNumbers(l1, l2):
    def make_node_to_num(l):
        head = l
        num = ""
        while True:
            num += str(head.val)
            if head.next:
                head = head.next
            else:
                break
        return num
    
    def make_num_to_node(num):
        root = head = None
        for i in range(len(num)):
            if i == 0:
                root = ListNode(num[i])
                head = root
            else:
                next = ListNode(num[i])
                head.next = next
                head = next
        return root
            
    n1 = make_node_to_num(l1)
    n2 = make_node_to_num(l2)

    total = int(n1[::-1]) + int(n2[::-1])

    ans = make_num_to_node(str(total)[::-1])
    return ans

l1 = ListNode(2, ListNode(4, ListNode(9)))
l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))

ans = addTwoNumbers(l1, l2)

head = ans
while head:
    print(head.val)
    head = head.next
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

result = factorial(5)
print(result)

input = "수박이박수"

# def is_palindrome(string):
#     return string[:] == string[::-1]

# def is_palindrome(string):
#     for i in range(len(string) // 2):
#         if string[i] == string[len(string) - 1 - i]:
#             continue
#         else:
#             return False
#     return True

# def is_palindrome(string):
#     n = len(string)
#     for i in range(n):
#         if string[i] != string[n - 1 - i]:
#             return False
#     return True

def is_palindrome(string):
    if len(string) <= 1:
        return True
    
    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])

print(is_palindrome(input))

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

    # def get_kth_node_from_last(self, k):
    #     length = 1
    #     cur = self.head
    #     while cur.next is not None:
    #         length += 1
    #         cur = cur.next
    #     check = length - k

    #     cur = self.head
    #     for _ in range(check):
    #         cur = cur.next
    #     return cur

    def get_kth_node_from_last(self, k):
        left = self.head
        right = self.head

        for _ in range(k-1):
            right = right.next
        
        while right.next is not None:
            left = left.next
            right = right.next
        
        return left

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# def is_available_to_order(menus, orders):
#     result = filter(lambda x: x not in menus, orders)
#     return len(list(result)) == 0

def is_available_to_order(menus, orders):
    set_menus = set(menus)

    for order in orders:
        if order not in set_menus: # O(1)
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)

numbers = [1, 1, 1, 1, 1]
target_number = 3


# def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
#     check = []

#     for n in array:
#         if not check:
#             check.append(n * 1)
#             check.append(n * -1)
#         else:
#             temp = []
#             for c in check:
#                 temp.append(n + c)
#                 temp.append(-n + c)
#             check = temp
#     return check.count(target)

# def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
#     count = 0
#     def check(array, idx, total):
#         nonlocal count # 상위 함수의 변수를 사용하겠다 선언
#         if len(array) == idx:
#             if total == target:
#                 count += 1
#             return

#         check(array, idx + 1, total + array[idx])
#         check(array, idx + 1, total - array[idx])
    
#     check(array, 0, 0)

#     return count

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    count = 0
    def check(array, idx, total):
        nonlocal count
        if len(array) == idx:
            if total == target:
                count += 1
            return
        check(array, idx + 1, total + array[idx])
        check(array, idx + 1, total - array[idx])

    check(array, 0, 0)
    return count



print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
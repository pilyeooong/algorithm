# from collections import deque

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Queue:
#     def __init__(self):
#         self.head = None
#         self.tail = None
    
#     def is_empty(self):
#         return self.head is None

#     def peek(self):
#         return self.head.data
    
#     def enqueue(self, value):
#         new_node = Node(value)
#         if self.is_empty():
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#     def dequeue(self):
#         delete_head = self.head
#         self.head = delete_head.next
#         return delete_head.data


# queue = Queue()
# queue.enqueue(5)
# queue.enqueue(4)
# queue.enqueue(3)
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())


# prices = [1, 2, 3, 2, 3]
# # answer = [4, 3, 1, 1, 0]

# # def get_price_not_fall_periods(prices):
# #     answer = []
# #     for i in range(len(prices)):
# #         seconds = 0
# #         for j in range(i + 1, len(prices)):
# #             seconds += 1
# #             if prices[i] > prices[j]:
# #                 break
# #         answer.append(seconds)
# #     return answer

# def get_price_not_fall_periods(prices):
#     answer = []
#     prices = deque(prices)

#     while prices:
#         seconds = 0
#         cur_price = prices.popleft()
#         for price in prices:
#             seconds += 1
#             if cur_price > price:
#                 break
#         answer.append(seconds)

#     return answer
    


# print(get_price_not_fall_periods(prices))

# print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
# print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
# print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))

# class Dict:
#     def __init__(self):
#         self.items = [None] * 8

#     def put(self, key, value):
#         index = hash(key) % len(self.items)
#         self.items[index] = value


# all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
# present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


# def get_absent_student(all_array, present_array):
#     dict = {}

#     for x in all_array:
#         if x not in dict:
#             dict[x] = True
    
#     for x in present_array:
#         del dict[x]
    
#     return list(dict.keys())[0]

# print(get_absent_student(all_students, present_students))

# print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
# print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))

def fibo_dp(n):
    dp = [0, 1, 1]

    for i in range(3, n + 1):
        dp.append(dp[i-1] + dp[i-2])
    
    print(dp)

    return dp[n]

result = fibo_dp(5)
print(result)
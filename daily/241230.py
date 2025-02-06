# from collections import deque
# import heapq

# ramen_stock = 4
# supply_dates = [4, 10, 15]
# supply_supplies = [20, 5, 10]
# supply_recover_k = 30

# # k 일 후에 공급이 정상화 되므로, 남은 재고 stock이 k보다 작거나 같으면 계속 공급 받아와야함
# def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    
#     answer = 0
#     last_added_date_index = 0
#     heap_supplies = []

#     while stock <= k:
#         while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
#             heapq.heappush(heap_supplies, -supplies[last_added_date_index])
#             last_added_date_index += 1

#         answer += 1
#         supply = heapq.heappop(heap_supplies)
#         stock += -supply

#     return answer


# print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
# print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
# print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
# print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))

# current_r, current_c, current_d = 7, 4, 0
# current_room_map = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#     [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

# # 1. 현재 위치를 청소한다.
# # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
# #     a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
# #     b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
# #     c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# #     d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
# # 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.


# def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
#     answer = 0
#     # 왼쪽 회전 시 방향
#     turn = {
#         0: 3, # 북
#         1: 0, # 동
#         2: 1, # 서
#         3: 2  # 남
#     }
#     # 후진 시 방향
#     back = {
#         0: 2,
#         1: 3,
#         2: 0,
#         3: 1
#     }
#     directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#     row = len(room_map)
#     col = len(room_map[0])

#     visited = [[False] * col for _ in range(row)]

#     q = deque()
#     q.append((r,c))
#     visited[r][c] = True
#     answer += 1
#     cur_d = d

#     while q:
#         x, y = q.popleft()

#         for i in range(4):
#             cur_d = turn[cur_d]
#             dx, dy = directions[cur_d]
#             next_x, next_y = x + dx, y + dy
#             if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col and visited[next_x][next_y] == False and room_map[next_x][next_y] == 0:
#                 q.append((next_x, next_y))
#                 visited[next_x][next_y] = True
#                 answer += 1
#                 break
#             elif i == 3:
#                 dx, dy = directions[back[cur_d]]
#                 next_x, next_y = x + dx, y + dy
#                 q.append((next_x, next_y))

#                 if room_map[next_x][next_y] == 1:
#                     return answer

#     return answer


# # 57 가 출력되어야 합니다!
# print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
# current_room_map2 = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#     [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]
# print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,3,1,current_room_map2))
# current_room_map3 = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#     [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]
# print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7,4,1,current_room_map3))
# current_room_map4 = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
#     [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]
# print("정답 = 25 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,2,0,current_room_map4))

seat_count = 9
vip_seat_array = [4, 7]

# 123 4 56 7 89
# fibo(3) * fibo(2) * fibo(2)
def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    answer = 1
    cur_index = 0
    
    def fibo(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return fibo(n-2) + fibo(n - 1)

    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        ways = fibo(fixed_seat_index - cur_index)
        answer *= ways
        cur_index = fixed_seat_index + 1
    
    answer *= fibo(total_count - cur_index)

    return answer


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
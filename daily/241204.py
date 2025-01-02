n = 6
times = [7, 10]

# left, right = 1, 60 
# mid = 30 
# people = [4, 3]

# def solution(n, times):
#     answer = 0
    
#     if len(times) >= n:
#             return max(times)

#     while n > 0:
#         answer += 1
#         for time in times:
#             if  answer % time == 0:
#                 n -= 1
        # 
    # return answer

# def solution(n, times):
#     # 최소 시간과 최대 시간을 정의
#     left, right = 1, max(times) * n  # 최대 시간은 가장 느린 심사관이 모든 사람을 처리할 때
    
#     answer = right
    
#     while left <= right:
#         mid = (left + right) // 2  # 중간 시간을 계산

#         people = sum(mid // time for time in times) # mid 시간 내에 처리할 수 있는 사람 수 계산
        
#         if people >= n:  # 처리 가능한 사람이 n명 이상이면
#             answer = mid  # 최소 시간을 갱신
#             right = mid - 1  # 시간을 더 줄일 수 있는지 탐색
#         else:
#             left = mid + 1  # 시간을 늘려야 함
            
#     return answer

def solution(n, times):
    left, right = 1, max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        available = sum(mid // time for time in times)
        
        if available >= n:
            answer = mid
            right  = mid - 1
        else:
            left = mid + 1
        
    return answer

print(solution(n, times))
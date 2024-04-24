import heapq


# def solution(jobs):
#     answer = 0

#     pq = []

#     cur_time = 0
#     count = 0
#     start = -1
#     while count < len(jobs):
#         for job in jobs:
#             if start < job[0] <= cur_time:
#                 heapq.heappush(pq, (job[1], job[0]))
#         if pq:
#             need_duration, point = heapq.heappop(pq)
#             start = cur_time
#             cur_time += need_duration
#             answer += cur_time - point
#             count += 1
#         else:
#             cur_time += 1
#     return answer // len(jobs)


jobs = [[0, 3], [1, 9], [2, 6]]


def solution(jobs):
    answer = 0

    cur = 0
    start = -1
    done = 0

    pq = []

    while done < len(jobs):
        for job in jobs:
            if start < job[0] <= cur:
                heapq.heappush(pq, (job[1], job[0]))

        if pq:
            duration, point = heapq.heappop(pq)
            start = cur
            cur += duration
            answer += cur - point
            done += 1
        else:
            cur += 1

    return answer // len(jobs)


print(solution(jobs))

import math


def solution(progresses, speeds):
    answer = []

    need_days = []
    for i in range(len(progresses)):
        need_day = math.ceil((100 - progresses[i]) / speeds[i])
        need_days.append(need_day)

    count = 1
    max_days = need_days[0]
    for i in range(1, len(need_days)):
        if need_days[i] > max_days:
            max_days = need_days[i]
            answer.append(count)
            count = 1
        else:
            count += 1
    answer.append(count)
    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
# progresses = [93, 30, 55]
# speeds = [1, 30, 5]

print(solution(progresses, speeds))

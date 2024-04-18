from collections import deque


def solution(priorities, location):
    answer = 0

    new_priorities = []
    for i, priority in enumerate(priorities):
        new_priorities.append((i, priority))

    # while new_priorities:
    #     max_priority = max(new_priorities, key=lambda x: x[1])

    #     priority = new_priorities.pop(0)
    #     if priority[1] < max_priority[1]:
    #         new_priorities.append(priority)
    #     else:
    #         answer += 1
    #         if priority[0] == location:
    #             return answer

    while new_priorities:
        priority = new_priorities.pop(0)

        if any(priority[1] < x[1] for x in new_priorities):
            new_priorities.append(priority)
        else:
            answer += 1
            if priority[0] == location:
                return answer

    return answer


# priorities = [2, 1, 3, 2]
# location = 2
priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))

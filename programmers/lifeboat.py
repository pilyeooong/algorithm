def solution(people, limit):
    answer = 0
    people.sort()

    l = 0
    r = len(people) - 1

    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
        else:
            r -= 1
        answer += 1

    return answer


# people = [70, 50, 80, 50]
people = [50, 50, 70, 80]
limit = 100

print(solution(people, limit))

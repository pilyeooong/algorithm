def solution(progresses, speeds):
    answer = []

    done = []
    while progresses:
        if progresses[0] < 100:
            if done:
                answer.append(len(done))
                done = []
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        else:
            progress = progresses.pop(0)
            speeds.pop(0)
            done.append(progress)
    if done:
        answer.append(len(done))

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))

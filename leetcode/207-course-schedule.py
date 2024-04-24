from collections import deque

numCourses = 2
prerequisites = [[1, 0]]


def solution(numCourses, prerequisites):
    ans = []
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses

    for i in range(len(prerequisites)):
        graph[prerequisites[i][1]].append(prerequisites[i][0])
        indegree[prerequisites[i][0]] += 1

    q = deque()

    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        ans.append(cur)
        for x in graph[cur]:
            indegree[x] -= 1
            if indegree[x] == 0:
                q.append(x)

    return len(ans) == numCourses


print(solution(numCourses, prerequisites))

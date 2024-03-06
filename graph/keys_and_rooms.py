from collections import deque


def solution(rooms):
    rooms_count = len(rooms)

    # list in 은 list의 크기에 따라 시간복잡도가 차이날수있음
    # 사전에 리스트를 초기화하거나, dict를 활용해 해시테이블 형태로 사용이 가능함
    visited = [False for _ in range(rooms_count)]

    def dfs(n):
        visited[n] = True

        # key로 포함된 지점만 갈테니 아래 코드는 굳이 필요없을듯
        # [keys.append(x) for x in rooms[n] if x not in keys]

        for x in rooms[n]:
            # if visited[x] == False and x not in keys:
            if visited[x] == False:
                dfs(x)

    def bfs(n):
        q = deque()
        q.append(n)
        visited[n] = True

        while q:
            cur_room = q.popleft()
            for key in rooms[cur_room]:
                if key not in q and visited[key] == False:
                    q.append(key)
                    visited[key] = True

    bfs(0)
    print(visited)

    if False in visited:
        return False

    return True


# rooms = [[0], [2], [3], []]
# rooms = [[1, 3], [3, 0, 1], [2], [0]]
rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]

print(solution(rooms))

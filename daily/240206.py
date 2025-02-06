from collections import deque

def get_one_count_from_binary(check, n):
    if n < 2:
        return n

    if n in check:
        return check[n]
    
    count = get_one_count_from_binary(check, n // 2) + n % 2
    check[n] = count

    return count

def get_one_count_from_binary_under_n(n):
    check = {}
    answer = 0
    target_count = get_one_count_from_binary(check, n)

    for i in range(n, 0, -1):
        count = get_one_count_from_binary(check, i)
        if count == target_count:
            answer += 1
    
    return answer

ans = get_one_count_from_binary_under_n(10)
print(ans)


def check_perfect_sentence(sentence):
    check = {}
    for i in range(ord('a'), ord('z') + 1):
        check[chr(i)] = 0

    no_space_sentence = sentence.replace(" ", "")
    for c in no_space_sentence:
        lower_c = c.lower()
        check[lower_c] += 1
    
    ans = []
    for k, v in check.items():
        if v == 0:
            ans.append(k)
    
    if len(ans) == 0:
        return 'perfect'
    
    return ans

ans = check_perfect_sentence('Hello World') 
print(ans)

v = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1]
    ]

def find_white_spaces_width(v):
    row = len(v)
    col = len((v[0]))

    visited = [[False] * col for _ in range(row)]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        count = 1

        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            cur_x, cur_y = q.popleft()

            for dx, dy in deltas:
                next_x, next_y = cur_x + dx, cur_y + dy

                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col and v[next_x][next_y] == 1 and visited[next_x][next_y] == False:
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = 1
                    count += 1
        return count

    width_list = []
    for x in range(row):
        for y in range(col):
            if v[x][y] == 1 and visited[x][y] == False:
                width = bfs(x, y)
                width_list.append(width)
    
    return [len(width_list), max(width_list)] # 영역의 갯수와, 영역 최대 넓이를 반환한다.

ans = find_white_spaces_width(v) 
print(ans)


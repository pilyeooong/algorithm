n,k = 5, 3
def time(n,k):
    count = 0

    for h in range(0, n+1):
        if h < 10:
            str_h = "0" + str(h)
        else:
            str_h = str(h)
        for m in range(0, 60):
            if m < 10:
                str_m = "0" + str(m)
            else:
                str_m = str(m)
            for s in range(0, 60):
                if s < 10:
                    str_s = "0" + str(s)
                else:
                    str_s = str(s)
                if str(k) in str_h + str_m + str_s:
                    count += 1
    return count

print(time(n,k))

def guild(l):
    answer = 0

    l.sort()

    group = []
    for i in range(len(l)):
        group.append(l[i])
        if l[i] <= len(group):
            answer += 1
            group = []

    return answer

# print(guild([2,3,1,2,2]))
print(guild([1,2,3,3]))

def keys_and_room(rooms):
    answer = False
    visited = [False for _ in range(len(rooms))]
    def dfs(idx):
        if visited[idx]:
            return

        visited[idx] = True
        for key in rooms[idx]:
            dfs(key)
        
        return
    
    dfs(0)
    
    if False not in visited:
        answer = True

    return answer

rooms = [[1],[2],[3],[]] # true
rooms = [[1,3],[3,0,1],[2],[0]] # false
print(keys_and_room(rooms))


def up_down_left_right(n, plans):
    move = {
        'L': (0,-1),
        'R': (0,1),
        'U': (-1,0),
        'D': (1,0),
    }
    row = col = n

    x,y = 1,1

    for plan in plans:
        move_x, move_y = move[plan]
        next_x, next_y = x + move_x, y + move_y

        if next_x <= row and next_x >= 1 and next_y <= col and next_y >= 1:
            x,y = next_x, next_y
    return x, y

n = 5
plans = ['R','R','R','U','D','D']
print(up_down_left_right(n, plans))

l = [1,2,3]
print(l[1:5])

def substring(s):
    answer = 0
    for i in range(len(s)):
        temp = s[i]
        for j in range(i + 1, len(s)):
            if s[j] not in temp:
                temp += s[j]
            else:
                break
        answer = max(answer, len(temp))
    
    return answer


s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
s = " "
print(substring(s))


nums = [1,2,3,4]
ans = []
def permutation(cur):
    if len(cur) == len(nums):
        ans.append(cur[:])
        return

    for num in nums:
        if num not in cur:
            cur.append(num)
            permutation(cur)
            cur.pop()
    return ans

print(permutation([]))

def three(l, target):
    for i in range(len(l)-2):
        for j in range(i+1, len(l) - 1):
            for k in range(j+1, len(l)):
                if l[i] + l[j] + l[k] == target:
                    return [i,j,k]

l = [4,9,7,5,1]
k = 15
print(three(l,k))
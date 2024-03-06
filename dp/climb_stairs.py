def climbStairs(n: int) -> int:
    memo = {}
    if n <= 0:
        return 0
    if n == 1:
        memo[n] = 1
    if n == 2:
        memo[n] = 2
    if n not in memo:
        memo[n] = climbStairs(n - 1) + climbStairs(n - 2)

    return memo[n]


def bottom_up_climb_stairs(n):
    memo = {}
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        for i in range(3, n + 1):
            memo[i] = bottom_up_climb_stairs(i - 1) + bottom_up_climb_stairs(i - 2)
    return memo[n]


print(bottom_up_climb_stairs(5))

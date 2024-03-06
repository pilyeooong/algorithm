# costs = [10, 15, 20, 17]
costs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]


memo = {}


def min_cost_climbing_stairs(n):
    if n == 0 or n == 1:
        return 0

    if n not in memo:
        memo[n] = min(
            min_cost_climbing_stairs(n - 2) + costs[n - 2],
            min_cost_climbing_stairs(n - 1) + costs[n - 1],
        )

    return memo[n]


print(min_cost_climbing_stairs(2))

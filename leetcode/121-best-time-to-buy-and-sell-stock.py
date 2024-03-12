prices = [7, 1, 5, 3, 6, 4]


def solution(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


print(solution(prices))

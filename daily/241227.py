from collections import deque
shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


# def get_max_discounted_price(prices, coupons):
#     sorted_prices = sorted(prices, reverse=True)
#     sorted_coupons = sorted(coupons, reverse=True)

#     total = 0
#     for idx, price in enumerate(sorted_prices):
#         if idx < len(sorted_coupons):
#             total += price * ((100 - sorted_coupons[idx]) / 100)
#         else:
#             total += price
#     return int(total)

def get_max_discounted_price(prices, coupons):
    sorted_prices = deque(sorted(prices))
    sorted_coupons = deque(sorted(coupons))

    total = 0
    while sorted_coupons:
        if sorted_prices:
            coupon = sorted_coupons.pop()
            price = sorted_prices.pop()
            total += price * ((100 - coupon) / 100)
        else:
            break

    total += sum(sorted_prices)

    return int(total)

print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))


def is_correct_parenthesis(string):
    stack = []

    for s in string:
        if s == "(":
            stack.append(")")
        elif stack and s == ")":
            stack.pop()
        else:
            return False
    return not stack


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))

def get_melon_best_album(genre_array, play_array):
    genres = {}
    plays = {}

    for idx, genre in enumerate(genre_array):
        if genre not in genres:
            genres[genre] = [(idx, play_array[idx])]
        else:
            genres[genre].append((idx, play_array[idx]))
            genres[genre] = sorted(genres[genre], key=lambda x: (-x[1], x[0]))

        if genre not in plays:
            plays[genre] = play_array[idx]
        else:
            plays[genre] += play_array[idx]
    
    ranked_genres = sorted(plays, key=lambda x: -plays[x])

    ans = []

    for idx, genre in enumerate(ranked_genres):
        for i in range(2):
            try:
                ans.append(genres[genre][i][0])
            except:
                break
    return ans


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))
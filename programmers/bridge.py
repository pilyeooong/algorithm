bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]


def solution(bridge_length, weight, truck_weights):
    second = 0
    stack = [0] * bridge_length

    while truck_weights:
        stack.pop(0)

        if len(stack) < bridge_length and sum(stack) + truck_weights[0] <= weight:
            truck_weight = truck_weights.pop(0)
            stack.append(truck_weight)
        else:
            stack.append(0)
        second += 1

    second += bridge_length

    return second


print(solution(bridge_length, weight, truck_weights))

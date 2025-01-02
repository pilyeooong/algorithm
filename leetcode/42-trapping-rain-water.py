height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [3, 2, 0, 1, 2]
height = [1,8,6,2,5,4,8,3,7]


def solution(height):
    volume = 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume


print(solution(height))

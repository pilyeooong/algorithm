from itertools import permutations


def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def solution(numbers):
    permutation_set = set(
        [
            int("".join(item))
            for i in range(7)
            for item in set(permutations(list(numbers), i + 1))
        ]
    )
    ans = 0
    for number in list(permutation_set):
        if isPrime(number):
            ans += 1

    return ans


numbers = "011"

print(solution(numbers))

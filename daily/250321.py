def reverse_integer(n):
    answer = 0

    while n > 0:
        mod = n % 10
        answer = answer * 10 + mod
        n //= 10

    return answer

result = reverse_integer(12345)
print(result)
print(result == 54321)
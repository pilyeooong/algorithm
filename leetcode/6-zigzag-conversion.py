def convert(s, num_rows):
    check = ['' for _ in range(num_rows)]
    if num_rows == 1 or len(s) == 1:
        return s

    cal = -1
    idx = 0
    for c in s:
        check[idx] += c
        if idx == num_rows - 1 or idx == 0:
            cal *= -1
        idx += cal

    print(check)
    
    return ''.join(check)
s = "PAYPALISHIRING"
converted = convert(s, 3)
print(converted)
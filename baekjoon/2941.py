s = "ljes=njak"

l = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

s = input()
for i in l:
    while i in s:
        s = s.replace(i, "1")
print(len(s))

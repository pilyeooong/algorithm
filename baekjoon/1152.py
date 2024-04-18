import re

s = input()

s = "The Curious Case of Benjamin Button."


def solution(s):
    l = re.sub(r"[^\w]", " ", s).split()
    print(l)
    print(len(l))


solution(s)

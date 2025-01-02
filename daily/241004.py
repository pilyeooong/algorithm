# def valid_parentheses(s):
#     l = []
#     for c in s:
#         if c == '(':
#             l.append(')')
#         elif c == '[':
#             l.append(']')
#         elif c == '{':
#             l.append('}')
#         elif not l or l.pop() != c:
#             return False
#     return not l

    
# print(valid_parentheses('{()[]})'))

def valid_parentheses(s):
    l = []
    for c in s:
        if c == '(':
            l.append(')')
        elif c == '{':
            l.append('}')
        elif c == '[':
            l.append(']')
        elif not l or l.pop() != c:
            return False
    return not l

print(valid_parentheses('{()[]})'))
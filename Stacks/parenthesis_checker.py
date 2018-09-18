# Checks if parenthesis are balanced
from stack import Stack
paren_str = input('Enter a parenthesis string:\n')

def is_match(a, b):
    if a=='[' and b==']':
        return True
    if a=='(' and b==')':
        return True
    if a=='{' and b=='}':
        return True

def is_paren_balanced(paren_str):
    s = Stack()
    for i in paren_str:
        if i in '([{':
            s.push(i)
        else:
            if s.is_empty():
                return False
            else:
                if not is_match(s.pop(), i):
                    return False

    return True

print(is_paren_balanced(paren_str))
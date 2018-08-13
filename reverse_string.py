# Reverse input string using stack
from stack import Stack
string = input('Enter string to reverse:\n')

def reverser(string):
    s = Stack()
    for i in string:
        s.push(i)
    rev = ''
    while not s.is_empty():
        rev += str(s.pop())
    return rev

print(reverser(string))

# without using stacks
print(string[::-1])
from stack import Stack
s = Stack()
num = input('Enter number:')

def find_binary(num):

    while num>0:
        rem = num % 2
        s.push(rem)
        num = num // 2

    binrep = ''
    while not s.is_empty():
        binrep += str(s.pop())
    return(binrep)

print(find_binary(int(num)))
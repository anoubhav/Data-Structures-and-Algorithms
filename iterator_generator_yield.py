class Powtwo:
    """ Create a class to implement an iterator of a power of two """
    def __init__(self, max = 0):
        self.max = max
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n<=self.max:
            self.n += 1
            return 2**(self.n - 1)
        else:
            raise StopIteration
        self.n += 1

a = Powtwo(10)
# for i in a:
#     print(i)

# for i in (2**x for x in range(11)):
#     print(i)

# def PowTwoGen(max=0):
#     n = 0
#     while n <= max:
#         yield 2 ** n
#         n += 1

# def all_pyramids():
#     h = 1
#     while True:
#         yield (3*(h**2) + h)//2
        # h += 1

# sum of squares of fibonacci numbers
def fibo(n):
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x+y
        yield x

def squares(n):
    for num in n:
        yield num**2

print(sum(squares(fibo(4))))


# for i, height in enumerate(all_pyramids()):
#     print(height)
#     if i == 10:
#         break

# for i in PowTwoGen(10):
#     print(i)
# def my_gen():
#     n = 1
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n

#     n += 1
#     print('This is printed second')
#     yield n

#     n += 1
#     print('This is printed at last')
#     yield n

# for item in my_gen():
#     print(item)
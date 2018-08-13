def fibonacci_recursive(n):
    if n < 0:
        raise ValueError('Invalid index!')
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    if n < 0:
        raise ValueError('Invalid index!')
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(n-1):
        c = a + b
        a = b
        b = c
    return c
print(fibonacci_recursive(10))
print(fibonacci_iterative(10))
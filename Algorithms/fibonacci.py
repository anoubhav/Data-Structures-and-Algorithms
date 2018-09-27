def FibonacciRecursive(n):
    if n <= 1:
        return n
    return FibonacciRecursive(n-1) + FibonacciRecursive(n-2)

def FibonacciIterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n-1):
        c = a + b
        a, b = b, c
    return c

if __name__ == '__main__':
    from time import clock
    num = int(input('Which fibonacci number to compute? '))
    t1   = clock()
    soln = FibonacciIterative(num)
    t2   = clock()
    print(f'\n{num}th fibonacci number: {soln}')
    print(f'Time taken by Iterative approach: {t2-t1:.5f}')

    t1   = clock()
    soln = FibonacciRecursive(num)
    t2   = clock()
    print(f'Time taken by Recursive approach: {t2-t1:.5f}')

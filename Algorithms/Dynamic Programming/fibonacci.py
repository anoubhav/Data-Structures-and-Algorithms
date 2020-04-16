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

def FibonacciMemo(n):
    if n<=1:
        return n
    if F[n]:
        return F[n]
    F[n] = FibonacciMemo(n-1) + FibonacciMemo(n-2)
    return F[n]
    
if __name__ == '__main__':
    from time import time
    # "Fib sequence starts from 0"

    # num = 30+ significant difference between recursive approach vs. iterative & DP
    num = int(input('Which fibonacci number to compute? '))
    t1   = time()
    soln = FibonacciIterative(num-1)
    t2   = time()
    print(f'\n{num}th fibonacci number: {soln}')
    print(f'Time taken by Iterative approach: {t2-t1:.5f}')

    t1   = time()
    soln2 = FibonacciRecursive(num-1)
    t2   = time()
    print(f'Time taken by Recursive approach: {t2-t1:.5f}')

    F = [0]*num
    t1   = time()
    soln3 = FibonacciMemo(num-1)
    t2   = time()
    print(f'Time taken by Memoization approach: {t2-t1:.5f}')
    assert soln == soln2 == soln3



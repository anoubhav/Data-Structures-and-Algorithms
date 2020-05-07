# Given a set of coin values = {c1, c2, c3, .., ck} and a target sum of money n, our task is to
# form the sum n using as few coins as possible.

from math import inf
from time import time

def recursive(coins, target):
    # Exponential time complexity
    if target<0:
        return inf
    if target == 0:
        return 0

    best = inf
    for c in coins:
        best = min(best, recursive(coins, target - c) + 1)
    return best

def memoization(coins, target):
    # O(N*k) time complexity. N is the target and k is length of coins.
    if target<0:
        return inf
    if target == 0:
        return 0
    if value[target]!=-1:
        return value[target]
    
    best = inf
    for c in coins:
        best = min(best, memoization(coins, target - c) + 1)
    value[target] = best

    return value[target]

def iterative(coins, target):
    value[0] = 0 # recursion base condition
    for i in range(1, target+1):
        value[i] = inf
        for c in coins:
            if i-c>=0:
                value[i] = min(value[i], value[i-c]+1)
    return value[target]

def construct_solution(coins, target):
    value[0] = 0
    for i in range(1, target + 1):
        value[i] = inf
        for c in coins:
            if i - c>=0 and value[i-c] + 1 < value[i]:
                value[i] = value[i-c] + 1
                first[i] = c

if __name__ == '__main__':
    coins = [2, 3, 4, 7, 11]
    target = 37

    # Recursion
    t = time()
    print(f'Recursive Soln = {recursive(coins, target)}; Time taken: {time() - t}')

    # Memoization
    # The only thing changing is the target in the recursive calls thus our memoization table only contains this dimension.
    value = [-1]*(target+1)
    t = time()
    print(f'Memoization Soln = {memoization(coins, target)}; Time taken: {time() - t}')

    # Iterative solution
    t = time()
    print(f'Iterative Soln = {iterative(coins, target)}; Time taken: {time() - t}')

    # Construct the solution, i.e., also return the set of coins required to obtain target.
    # The array stores the first coin in the optimal solution for each sum of money
    first = [0]*(target + 1) 
    construct_solution(coins, target)
    soln = []
    while target:
        coin = first[target]
        soln.append(coin)
        target -= coin
    print('Construction:', soln)
    
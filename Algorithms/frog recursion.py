""" There are 10 stones in a line leading across the river, separated by 1 foot. He can either jump to the next stone or jump over a stone, and if he jumps over a stone he must land on the next one. The furthest he can jump is 2 feet. Also, he always moves forward (toward the other side of the river). In how many different ways can he jump exactly 11 feet to the other side of the river? """

# Recurrence relation F(n+2) = F(n+1) + F(n)

def frog_path(n):
    if n < 0:
        raise ValueError('Invalid index')
    if n == 1:
        return 1
    if n == 2:
        return 2
    return frog_path(n-1) + frog_path(n-2)

import time
t = time.time()
print(frog_path(40))
print(time.time()-t)

# python - 66.5 seconds
# pypy3 - 2.3seconds
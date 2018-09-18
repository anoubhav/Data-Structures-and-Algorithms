""" Finds all prime numbers less than or equal to n. Old technique which is efficient at finding small prime numbers. Better and newer algorithm is the sieve of atkins."""

import time

def sieve_of_eratosthenes(n):
    start_time = time.time()
    # starting with from 2 till n 
    is_prime = [True]*(n-1)
    p = 2

    while True:
        multiplier = 2
        multiple = p*multiplier #(2p, 3p, 4p,..)

        while multiple<=n:
            is_prime[multiple-2] = False
            multiplier += 1
            multiple = p*multiplier
        
        for i, prime in enumerate(is_prime):
            if prime and i+2>p:
                p = i+2
                break
        else:
            break
    end_time = time.time()
    for i, prime in enumerate(is_prime):
        if prime: print (i+2)

    print('Total time:{0:0.5f}'.format(end_time-start_time))

sieve_of_eratosthenes(10000)
# Rod Cutting Problem
#  Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the  maximum value obtainable by cutting up the rod and selling the pieces. 

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
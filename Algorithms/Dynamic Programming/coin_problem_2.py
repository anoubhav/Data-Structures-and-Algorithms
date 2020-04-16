# calculate the total number of ways to produce a sum x using the coins {c1, c2, c3, .., ck}

def iterative(coins, target):
    for i in range(1, target + 1):
        value[i] = 0
        for c in coins:
            if i-c>=0:
                value[i] += (value[i-c])

    return value[target]
if __name__ == '__main__':
    coins = [1, 3, 4]
    target = 5
    
    value = [1]*(target + 1)
    print(iterative(coins, target))
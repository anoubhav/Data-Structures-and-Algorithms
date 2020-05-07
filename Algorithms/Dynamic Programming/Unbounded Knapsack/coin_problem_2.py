# calculate the total number of ways to produce a sum x using the coins {c1, c2, c3, .., ck}

def subset_sum_memoization(nums, total, n):
    if t[total][n]!=-1:
        return t[total][n]
    else:
        if total == 0:
            return 1
        if n==0 and total!=0:
            return 0
        
        if nums[n-1]>total:
            t[total][n] = subset_sum_memoization(nums, total, n-1)
            return t[total][n]
        else: 
            t[total][n] = subset_sum_memoization(nums, total-nums[n-1], n) + subset_sum_memoization(nums, total, n-1)
            return t[total][n]

def iterative(coins, target):
    for i in range(1, target + 1):
        value[i] = 0
        for c in coins:
            if i-c>=0:
                value[i] += (value[i-c])

    return value[target]
if __name__ == '__main__':
    coins = [1, 2, 3]
    target = 4
    
    value = [1]*(target + 1)
    print(iterative(coins, target))

    n = len(coins)
    t = [[-1]*(n+1) for _ in range(target+1)]
    print(subset_sum_memoization(coins, target, n))
    print(t)
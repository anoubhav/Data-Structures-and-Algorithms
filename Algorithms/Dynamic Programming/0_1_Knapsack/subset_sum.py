# Given a set of non-negative integers, and a value tot, determine if there is a subset of the given set with sum equal to given tot.

def subset_sum_recursive(nums, total, n):
    if total == 0:
        return 1
    if n==0 and total!=0:
        return 0
    
    if nums[n-1]>total:
        return subset_sum_recursive(nums, total, n-1)
    else:
        return max(subset_sum_recursive(nums, total-nums[n-1], n-1), subset_sum_recursive(nums, total, n-1))

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
            t[total][n] = max(subset_sum_memoization(nums, total-nums[n-1], n-1), subset_sum_memoization(nums, total, n-1))
            return t[total][n]

def subset_sum_iterative(nums, total, n):
    for i in range(1, n+1):
        for j in range(1, total+1):
            if nums[i-1]>total:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = max(t[i-1][j], t[i-1][j - nums[i-1]])
    return t[n][total]

if __name__ == '__main__':
    nums = [1, 3, 4, 5, 11, 13, 63, 30, 45, 33, 45, 7, 8, 9, 111, 56]
    total = 201
    n = len(nums)

    # Recursive solution
    print(subset_sum_recursive(nums, total, n))

    # Memoization: (W+1)x(n+1) lookup table
    t = [[-1]*(n+1) for _ in range(total+1)]
    print(subset_sum_memoization(nums, total, n))


    # Iterative solution: (n+1)x(W+1) lookup table
    t = [[-1]*(total+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(total):
            if j == 0: 
                t[i][j] = 1
            if i==0 and j!=0:
                t[i][j] = 0
    
    print(subset_sum_iterative(nums, total, n))
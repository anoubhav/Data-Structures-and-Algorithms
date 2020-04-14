# 0-1 Knapsack problem: Maximize the value of items stored in a knapsack by either selecting/leaving items from a list.

# wt - array of item weights
# val - array of item value
# W - total capacity of knapsack
# n - number of elements in array

def recursive_knapsack(wt, val, W, n):
    # For base condition think of the lowest valid input to the function. Either the number of items can be 0 or the capacity of the knapsack can be 0.
    # In such a case no value can be added to knapsack.
    if n==0 or W==0:
        return 0
    
    if wt[n-1]>W:
        # If item weight more than capacity, W is unchanged, number of items is reduced
        return recursive_knapsack(wt, val, W, n-1)

    elif wt[n-1]<=W:
        # If item weight less than capacity, either we can include it in the knapsack or we can exclude it. We want to maximize the value from both 
        # possible options
        
        include = val[n-1] + recursive_knapsack(wt, val, W-wt[n-1], n-1)
        exclude = recursive_knapsack(wt, val, W, n-1)

        return max(include, exclude)


def memoization_knapsack(wt, val, W, n):
    # Before making the usual recursive call, check if the value has been computed earlier. If not do the usual.
    # NOTE: The difference in the code between recursive and memoization is only a couple of lines. The core logic is the same.

    if t[W][n] != -1:
        return t[W][n]
    else:
        if n==0 or W==0:
            t[W][n] = 0
            return t[W][n]
        
        if wt[n-1]>W:
            t[W][n] = recursive_knapsack(wt, val, W, n-1)
            return t[W][n]

        elif wt[n-1]<=W:
            
            include = val[n-1] + recursive_knapsack(wt, val, W-wt[n-1], n-1)
            exclude = recursive_knapsack(wt, val, W, n-1)
            t[W][n] = max(include, exclude)
            return t[W][n]


def iterative_knapsack(wt, val, W, n):
    # Take the equations in recursive_knapsack. Change the recursive call to the table t. CHange all instances of n to i and W to j.
    # Also the table t was initialized using the base conditions of recursive_knapsack.

    for i in range(1, n+1):
        for j in range(1, W+1):
            # if weight of item less than knapsack
            if wt[i-1]<=j:
                include = val[i-1] + t[i-1][j-wt[i-1]]       # val[n-1] + recursive_knapsack(wt, val, W-wt[n-1], n-1)
                exclude = t[i-1][j]                          # recursive_knapsack(wt, val, W, n-1)
                t[i][j] = max(include, exclude)
            else:
                t[i][j] = t[i-1][j]                          # recursive_knapsack(wt, val, W, n-1)

    return t[n][W]


if __name__ == '__main__':
    wt  = [1, 4, 5, 7, 12, 15, 8, 11]
    val = [1, 3, 4, 5, 13, 15, 9, 13]
    W = 30
    n = len(wt)

    ## Recursive 0/1 Knapsack solution
    print(recursive_knapsack(wt, val, W, n))

    ## Memoization = Recursion + Storage (Top-Down approach). 
    # Initializing a look-up table of dimension (W+1)x(n+1). Our answer will be stored in t[W][n].
    # The following lookup table was made because from the recursive solution, it is clear that ONLY the capacity (W) and number of items (n) 
    # changes for each function call.

    # the value for a given W,n can be 0. But, value cannot be negative.
    t = [[-1]*(n+1) for _ in range(W+1)]
    print(memoization_knapsack(wt, val, W, n))

    ## Tabulation/Iterative/Bottom-up 0/1 Knapsack.
    t = [[0]*(W+1) for _ in range(n+1)]
    print(iterative_knapsack(wt, val, W, n))


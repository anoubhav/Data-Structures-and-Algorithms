# Unbounded Knapsack  : Maximize the value of items stored in a knapsack by selecting/leaving items from a list WITH
# possibility of REPITITION

# wt - array of item weights
# val - array of item value
# W - total capacity of knapsack
# n - number of elements in array

# The code is the same as 0-1 Knapsack other than 1 small change. If an item is included into the knapsack, it can 
# be included again in the future as well. That is the only difference.


def recursive_unbounded_knapsack(wt, val, W, n):
    # For base condition think of the lowest valid input to the function. Either the number of items can be 0 or the capacity of the knapsack can be 0.
    # In such a case no value can be added to knapsack.
    if n==0 or W==0:
        return 0
    
    if wt[n-1]>W:
        # If item weight more than capacity, W is unchanged, number of items is reduced
        return recursive_unbounded_knapsack(wt, val, W, n-1)

    elif wt[n-1]<=W:
        # If item weight less than capacity, either we can include it in the knapsack or we can exclude it. We want to maximize the value from both 
        # possible options
        
        # include = val[n-1] + recursive_knapsack(wt, val, W-wt[n-1], n-1)  ## 0-1 Knapsack
        include = val[n-1] + recursive_unbounded_knapsack(wt, val, W-wt[n-1], n)    ## Unbounded
        exclude = recursive_unbounded_knapsack(wt, val, W, n-1)

        return max(include, exclude)

if __name__ == '__main__':
    wt  = [1, 4, 5, 7, 12, 15, 8, 11]
    val = [1, 3, 4, 5, 13, 15, 9, 13]
    W = 30
    n = len(wt)

    ## Recursive Unbounded Knapsack solution = 35, whereas 0-1 Knapsack solution = 31
    print(recursive_unbounded_knapsack(wt, val, W, n))
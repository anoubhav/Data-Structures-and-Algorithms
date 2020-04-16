# Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.

# Use the subset sum program to fill the table (n+1xW+1) upto sum(arr). for each column (w) check if its possible to obtain it,
# ,i.e., 1 is present in the column. See the column closest to the center (W//2) that is one of your partitions.

# To fill the (n+1xW+1) table it is essential to use iterative approach rather than memoization as when you execute top-down(memo)
# it does NOT need to make unnecessary function calls which do not help in evaluating the final question which is t[total][n].
# Whereas, the iterative (bottom-up) approach has to fill the entire table before reaching t[total][n].

# Thus dp_memo will return a table t with -1 still present in most places. Whereas, dp_iterative will return a complete table t.

def dp_memo(nums, total, n):
    # memo/storage
    if t[total][n]!=-1:
        return t[total][n]
    else:
        # recursion base conditions
        if total == 0:
            return 1
        elif total!=0 and n==0:
            return 0

        # code
        if nums[n-1]>total:
            exclude = dp_memo(nums, total, n-1)
            t[total][n] = exclude
            return t[total][n]
        else:
            include = dp_memo(nums, total - nums[n-1], n-1)
            exclude = dp_memo(nums, total, n-1)
            t[total][n] = max(include, exclude)
            return t[total][n]


def dp_iterative(nums, total, n):
    for i in range(1, total + 1):
        for j in range(1, n+1):
            if nums[j-1]>i:
                t[i][j] = t[i][j-1]
            else:
                t[i][j] = max(t[i][j-1], t[i-nums[j-1]][j-1])
    return t[total][n]

def get_min_subset_diff(nums, total, n):
    # Populate the table with the correct values, i.e., For a given (n, w) is a subset possible.
    # Only possible using bottom-up iterative approach.

    # Memoization: table t still contains -1
    # dp_memo(nums, total, n) 

    # Iteration
    dp_iterative(nums, total, n) # Fill the table
    
    # Which subsets are possible?
    lst = []
    for row in t:
        if sum(row)>0:
            lst.append(1)
        else:
            lst.append(0)
    
    mid = total//2
    ans = total

    for i in range(mid, -1, -1):
        if lst[i] == 1:
            ans = abs(total - 2*i)
            break
            
    return ans

if __name__ == '__main__':
    nums = [1, 2, 3, 3, 4] # P1 = (3, 3) ; P2 = (1, 2, 4) ; DIFF = 1

    n = len(nums)
    total = sum(nums)
    # memoization table
    # t = [[-1]*(n+1) for _ in range(total+1)]

    # recursion table: Initialize same as recursion base condition
    t = [[None]*(n+1) for _ in range(total+1)]

    for i in range(total + 1):
        for j in range(n+1):
            if i == 0:
                t[i][j] = 1
            if j==0 and i!=0:
                t[i][j] = 0
    
    print(get_min_subset_diff(nums, total, n))


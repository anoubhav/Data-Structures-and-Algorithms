# Given an array arr[] of length N and an integer X, the task is to find the number of subsets with sum equal to X.

# The code is exact same as subset_sum.py. The only difference is that the max() operation between including and excluding an 
# item is changed to SUM. You want to add all subsets which include an item and exclude an item to give a TOTAL.
# The initialization conditions are also same. As the no. of subsets when total is 0 is 1, null set. The no. of subsets
# of zero length array and total non-zero is zero.

def count_of_subset_sum_memoization(nums, total, n):
    if t[total][n]!=-1:
        return t[total][n]
    else:
        if total == 0:
            return 1
        if n==0 and total!=0:
            return 0
        
        if nums[n-1]>total:
            t[total][n] = count_of_subset_sum_memoization(nums, total, n-1)
            return t[total][n]
        else:    #### Change max() to + and you get count of subset instead of subset sum
            t[total][n] = count_of_subset_sum_memoization(nums, total-nums[n-1], n-1) + count_of_subset_sum_memoization(nums, total, n-1)
            return t[total][n]

if __name__ == '__main__':
    nums = [1, 2, 3, 3, 5]  #(3, 3), (1, 2, 3), (1, 2, 3), (1, 5)
    total = 6
    n = len(nums)

    t = [[-1]*(n+1) for _ in range(total+1)]
    print(count_of_subset_sum_memoization(nums, total, n))


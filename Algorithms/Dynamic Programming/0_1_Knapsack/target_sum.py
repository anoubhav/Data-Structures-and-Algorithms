# Given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

def count_of_subset_sum_memoization(nums, total, n):
    if t[n][total] != -1:
        return t[n][total]
    else:
        if total == 0:
            return 1
        if n==0 and total!=0:
            return 0

        if nums[n-1]>total:
            exclude = count_of_subset_sum_memoization(nums, total, n-1)
            t[n][total] = exclude
            return t[n][total]
        else:
            exclude = count_of_subset_sum_memoization(nums, total, n-1)
            include = count_of_subset_sum_memoization(nums, total - nums[n-1], n-1)

            t[n][total] = exclude + include
            return t[n][total]
            
if __name__ == '__main__':
    a = [1, 1, 1, 1, 1]
    S = 3
    n = len(a)
    # Equivalent to dividing the array a into two subsets (s1 and s2) such that the diff between them is S. Next we count 
    # the number of ways to obtain abs(s1-s2) = S using DP.
    ss = (S + sum(a))/2
    # if the required sum of the subset with integer values is floating point, not possible.
    if ss!=int(ss):
        print(0)
    # create a memoization table of size (n+1)x(ss + 1). Initialization same as recursion base condition.
    # ss = 0 -> 1 way and if n=0 & s!=0 -> 0 way
    else:
        t = [[-1]*(int(ss)+1) for _ in range(n+1)]
        print(count_of_subset_sum_memoization(a, int(ss), n))

# Count the number of subset with a given difference, i.e., find the number of ways to divide an array nums into two subsets
# s1 and s2 such that s1-s2 = diff

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
    nums = [1, 1, 3]
    diff = 1
    n = len(nums)

    # s1 - s2 = diff ; s1 + s2 = sum(nums). Thus, s1 = (diff + sum(nums))/2 = ss
    # The problem is reduced to counting the number of subsets with above sum.

    ss = (diff + sum(nums))/2
    # if the required sum of the subset with integer values is floating point, not possible.
    if ss!=int(ss):
        print(0)
    # create a memoization table of size (n+1)x(ss + 1). Initialization same as recursion base condition.
    # ss = 0 -> 1 way and if n=0 & s!=0 -> 0 way
    else:
        t = [[-1]*(int(ss)+1) for _ in range(n+1)]
        print(count_of_subset_sum_memoization(nums, int(ss), n))




# Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.

# Same as subset sum, we just have to find if a subset sum == sum of array//2. Thus, if sum of array is odd, it is not possible.

def eps_recursive(nums, total, n):
    if total == 0:
        return 1

    if n==0 and total!=0:
        return 0

    if nums[n-1]>total:
        return eps_recursive(nums, total, n-1)
    else:
        include = eps_recursive(nums, total - nums[n-1], n-1)
        exclude = eps_recursive(nums, total, n-1)
        return max(include, exclude)


if __name__ == '__main__':
    nums = [1, 5, 3]

    n = len(nums)
    total = sum(nums)

    if total%2==1: print('0')
    else:
        # Recursive solution
        print(eps_recursive(nums, total//2, n-1))

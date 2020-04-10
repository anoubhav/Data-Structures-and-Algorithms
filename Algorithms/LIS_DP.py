""" The task is to find the length of the longest subsequence in a given array of integers such that all elements 
of the subsequence are sorted in strictly ascending order. Source link: https://www.youtube.com/watch?v=4fQJGoeW5VE&t=1s """

# Below program has time complexity of O(n^2)
def IncreasingSubsequences(arr):
    """ Finds the LIS for all i in arr ending with arr[i].
    (list) -> (list of lists) """
    l = len(arr)
    L = list()

    # L[i] is the LIS of arr which ends with arr[i]. L[0] = [arr[0]]
    for i in range(l):
        L.append([arr[i]])

    for i in range(1, l):
        max_l = 0
        for j in range(i):
            if arr[j]<arr[i] and len(L[j])>max_l:
                max_l = len(L[j])
                L[i] = L[j] + [arr[i]]
    return L  

def LIS(L):
    max_length = 1
    for i in L:
        if len(i)>max_length:
            max_length = len(i)
            soln = i
    return max_length, soln

if __name__ == '__main__':

    arr = input().split(' ')
    temp = IncreasingSubsequences([int(i) for i in arr])
    LIS_len, soln = LIS(temp)
    print(' '.join([str(i) for i in soln]))


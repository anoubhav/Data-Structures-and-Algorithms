from time import time, clock

def CreateSortedArray(size = 100, max_gap = 100, likelihood = 3):
    """ Creates random sorted array of input size. max_gap is the maximum gap between two consecutive numbers in the array. 

    Also creates random search element which has likelihood:1 chance of being present in the random sorted array. Higher the input likelihood, higher is the probability for random search element to be present in array.

    (int, int) -> (list, int) """
    from random import randint, choice
    
    t1 = clock()
    arr = [randint(0, max_gap)] + [0]*(size-1)
    # Creates random sorted array
    for i in range(1, size):
        step_size = randint(0, max_gap)
        arr[i] = arr[i-1] + step_size
    t2 = clock()
    print(f'Time taken for creating random sorted array : {t2-t1:.5f}')

    # Creates random search element
    t1 = clock()
    search_elem = choice(arr + [randint(0, arr[-1]) for i in range(size//likelihood)])
    t2 = clock()
    print(f'Time taken for picking random search element: {t2-t1:.5f}')
    return arr, search_elem

def BinarySearchIterative(seq, elt, r):
    """ Returns index if item is present and -1 if not present. O(log n) runtime """
    l = 0
    while l<=r: 
        m = (l+r)//2
        if elt > seq[m]:
            l = m + 1
        elif elt < seq[m]:
            r = m - 1
        else:
            return m
    return -1
        
def BinarySearch(A, item):
    """ Return true is item is present in A and false if not present. O(log n) runtime"""
    if len(A) == 0:
        return False
    else:
        middle = len(A) // 2
        if A[middle] == item:
            return True
        if A[middle] > item:
            return BinarySearch(A[:middle], item)
        else:
            return BinarySearch(A[middle + 1:], item)

def LinearSearch(A, item):
    """ Linear search works for unsorted lists as well. Function returns index if item is present and -1 if not present. O(n^2) runtime """
    for i in range(len(A)):
        if A[i] == item:
            return i
    return -1

if __name__ == '__main__':

    # Uncomment below line to generate random sorted array and random search element. O(n) runtime.
    # arr, search_elem = CreateSortedArray(size = 10000, max_gap = 100, likelihood = 10)
    ## print('Array :' , arr,'\nSearch:', search_elem)

    arr, search_elem = [i for i in range(10000000)], 9999999

    # Binary Search
    t1   = clock()
    temp = BinarySearchIterative(arr, search_elem, len(arr))
    t2   = clock()
    print('Binary Search index:', temp, f', Time taken: {t2-t1:.5f}')

    # Linear Search
    t1  = clock()
    temp = LinearSearch(arr, search_elem)
    t2  = clock()
    print('Linear Search index:', temp, f', Time taken: {t2-t1:.5f}')
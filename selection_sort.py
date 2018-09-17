# Selection sort algorithm: O(n^2)

import random
import time

def create_array(size = 2000, max_num = 10000):
    return [random.randint(0, max_num) for _ in range(size)]

def selection_sort(arr):
    t1 = time.time()
    comparisons, swaps = 0, 0
    l = len(arr)
    for i in range(l-1):
        min_ind = i
        for j in range(i+1, l):
            if arr[j] < arr[min_ind]:
                comparisons += 1
                min_ind = j
        if min_ind != i:
            arr[i], arr[min_ind] = arr[min_ind], arr[i]
            comparisons+=1
            swaps += 1
    t2 = time.time()
    return arr, t2-t1, swaps, comparisons

def main():
    arr = create_array()
    unsorted_arr = arr.copy()
    sorted_arr, time_taken, swaps, comparisons = insertion_sort(arr)
    print('Before sorting   :', unsorted_arr)
    print('After sorting    :', sorted_arr)
    print('Time taken       :', time_taken)
    print('Swaps count      :', swaps)
    print('Comparisons count:', comparisons)

def average_time(iterations = 10):
    """ Computes average run time for sorting operation by calling selection_sort() method 'iterations' number of times
    (int) -> (float) """
    tot = 0
    for _ in range(iterations):
        arr = create_array()
        _, time_taken, _, _ = selection_sort(arr)
        tot += time_taken
        print(time_taken)
    return tot/iterations

if __name__ == '__main__':
    # main()

    # Comment below line if average run time is not needed
    print('Average time taken:', average_time())
        

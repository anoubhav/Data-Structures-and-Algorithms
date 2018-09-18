# Bubble sort algorithm: O(n^2)

import random
import time

def create_array(size = 2000, max_num = 10000):
    """ Returns random array of given size and elements upto max_num 
    (int, int) -> (list) """
    return [random.randint(0, max_num) for _ in range(size)]

def bubble_sort(arr):
    t1 = time.time()
    swaps, comparisons = 0, 0
    l = len(arr)
    for i in range(l-1):
        swapped = False
        for j in range(l-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                comparisons += 1
                swapped = True
        if swapped == False: break
    t2 = time.time()
    return arr, t2-t1, swaps, comparisons

def main():
    arr = create_array()
    unsorted_arr = arr.copy()
    sorted_arr, time_taken, swaps, comparisons = bubble_sort(arr)
    # print('Before sorting   :', unsorted_arr)
    # print('After sorting    :', sorted_arr)
    print('Time taken       :', time_taken)
    print('Swaps count      :', swaps)
    print('Comparisons count:', comparisons)

def average_time(iterations = 10):
    """ Computes average run time for sorting operation by calling bubble_sort() method 'iterations' number of times
    (int) -> (float) """
    tot = 0
    for _ in range(iterations):
        arr = create_array()
        _, time_taken, _, _ = bubble_sort(arr)
        tot += time_taken
        print(time_taken)
    return tot/iterations

if __name__ == '__main__':
    # main()

    # Comment below line if average run time is not needed
    print('Average time taken:', average_time())
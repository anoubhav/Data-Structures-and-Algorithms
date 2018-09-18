# Insertion sort algorithm: O(n^2)

import random
import time

def create_array(size = 2000, max_num = 10000):
    """ Returns random array of given size and elements upto max_num 
    (int, int) -> (list) """
    return [random.randint(0, max_num) for _ in range(size)]

def insertion_sort_assignment(arr):
    t1 = time.time()
    assignments, comparisons = 0, 0
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j>=0 and k<arr[j]:
            assignments += 1
            comparisons += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k
    t2 = time.time()
    return arr, t2-t1, assignments, comparisons


def main():
    arr = create_array()
    unsorted_arr = arr.copy()
    sorted_arr, time_taken, assignments, comparisons = insertion_sort_assignment(arr)
    # print('Before sorting   :', unsorted_arr)
    # print('After sorting    :', sorted_arr)
    print('Time taken       :', time_taken)
    print('Assignments count:', assignments)
    print('Comparisons count:', comparisons)

def average_time(iterations = 10):
    """ Computes average run time for sorting operation by calling insertion_sort_assignment() method 'iterations' number of times
    (int) -> (float) """
    tot = 0
    for _ in range(iterations):
        arr = create_array()
        _, time_taken, _, _ = insertion_sort_assignment(arr)
        tot += time_taken
        print(time_taken)
    return tot/iterations

if __name__ == '__main__':
    # main()

    # Comment below line if average run time is not needed
    print('Average time taken:', average_time())


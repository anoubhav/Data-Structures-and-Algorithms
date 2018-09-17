from selection_sort import selection_sort
from insertion_sort_swapping import insertion_sort_swap
from insertion_sort_assignment import insertion_sort_assignment
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quicksort3 import quicksort3
from time import clock
import random

def create_array(size = 2000, max_num = 1000):
    """ Returns random array of given size and elements upto max_num 
    (int, int) -> (list) """
    return [random.randint(0, max_num) for _ in range(size)]

def benchmark(n = [10, 100, 1000, 5000, 10000]):
    """ Benchmark the 6 sorting algorithms """

    times = {'bubble':[], 'selection':[], 'merge':[], 'quicksort3':[], 'insertion_swap':[], 'insertion_ass':[]}
    
    for size in n:
        a = create_array(size = size, max_num = 10*size)
        t0 = clock()
        bubble_sort(a)
        t1 = clock()
        times['bubble'].append(t1-t0)
        
        a = create_array(size = size, max_num = 10*size)
        t0 = clock()
        selection_sort(a)
        t1 = clock()
        times['selection'].append(t1-t0)

        a = create_array(size = size, max_num = 10*size)
        t0 = clock()
        merge_sort(a)
        t1 = clock()
        times['merge'].append(t1-t0)

        a = create_array(size = size, max_num = 10*size)
        t0 = clock()
        insertion_sort_swap(a)
        t1 = clock()
        times['insertion_swap'].append(t1-t0)

        a = create_array(size = size, max_num = 10*size)
        t0 = clock()
        insertion_sort_assignment(a)
        t1 = clock()
        times['insertion_ass'].append(t1-t0)

        a = create_array(size = size, max_num = 10*size)
        t0 = clock()
        quicksort3(a, 0, size)
        t1 = clock()
        times['quicksort3'].append(t1-t0)

    print(98*'_')
    print("n\tBubble\t   Insertion(s)\t\tInsertion(a)\t   Merge\tQuicksort3\tSelection")
    print(98*'_')
    for i, size in enumerate(n):
        print("%d\t%5.4f\t     %5.4f\t\t  %5.4f\t  %5.4f\t  %5.4f\t %5.4f"%(size, times['bubble'][i], times['insertion_swap'][i], times['insertion_ass'][i], times['merge'][i], times['quicksort3'][i], times['selection'][i]))

benchmark(n = [10, 100])



def quicksort(a):
    less, pivotlist, more = [], [], []
    len_arr = len(a)
    # Base case
    if len_arr <= 1:
        return a
    else:
        # Picking pivot element by 'Median of Three' or first element
        if len(a)>2:
            pivot = sorted([a[0], a[len_arr//2], a[-1]])[1]
        else:
            pivot = a[0]
        # Dividing elements to left and right of the pivot
        for i in a:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotlist.append(i)
        # Recursively calling the function for elements on both sides of the pivot
        less = quicksort(less)
        more = quicksort(more)
        return less + pivotlist + more

def create_array(size=1000000, max=10000000):
    from random import randint
    return [randint(0, max) for _ in range(size)]
import time 
t0 = time.time()
a = create_array()
s = quicksort(a)
t1 = time.time()

t2 = time.time()
a = [i for i in range(1000000)]
s = quicksort(a)
t3 = time.time()

""" While taking the first element as pivot in a presorted array. The size of the problem is only decreased by 1 for every pivot. This leads to a worst case complexity of O(N^2). We can't sort a presorted array of size 1000 in this case due to RecursionError: maximum recursion depth exceeded in comparison. This happens as explained above. Only decrease of 1 instead of an ideal pivot which decreases problem size to half.
One way to work around this pre-sorted sequence issue is to use Median of 3 method to select pivot """

print(f'Time taken to sort randomly generated array of size 1,000,000: {t1-t0}')
print(f'Time taken to sort pre-sorted array of size 1,000,000: {t3-t2}')

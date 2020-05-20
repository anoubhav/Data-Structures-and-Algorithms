a = [1, 3, 11, -1, 8]

## Selection Sort
# To make selection sort work, you had to make sure all the numbers in the unsorted segment of the array always stayed greater than or equal to the numbers in the sorted segment of the array.

# This algorithm is very stingy about swapping, only requiring n-1n−1 swap instructions to sort an array of length nn. This minimalism is only possible because the algorithm does a lot of work scanning the unsorted part of the array, making sure the correct element goes into the correct place.

# selection sort
def selection_sort(arr):
    for curr in range(len(a)-1):
        min_index = curr
        for i in range(curr+1, len(a)):
            if a[i] < a[min_index]:
                min_index=i
        
        a[curr], a[min_index] = a[min_index], a[curr]  # swap operation
    print(a) 

selection_sort(a.copy())


## Insertion sort
# you'll keep a sorted segment and an unsorted segment, and only ever look at the first number of the unsorted segment.

# The array can't be sliced and diced in order to do the "insertion" step of insertion sort. Instead, insertion is done with a cascade of swaps that continually push the new element (10, in our running example) down the sorted segment.

# Selection sort minimizes the number of swaps by repeatedly scanning the unsorted segment of the array.
# Insertion sort, the topic of this quiz, avoids this extra scanning by doing extra swaps as part of insertion into the sorted segment.


# Unlike selection sort, the cost of insertion sort — as measured in terms of the number of comparisons of two array elements — cannot be expressed as a function of the length of the array alone. It also depends on the contents of the array.

def insertion_sort(a):
    for curr in range(1, len(a)):
        i = curr
        while i>0 and a[i-1]>a[i]:
            a[i-1], a[i] = a[i], a[i-1]
            i -= 1
    print(a)

insertion_sort(a.copy())


# Sometimes, optimism is warranted! For sorting, the best-case number of comparisons is a good guide if an array is known to be sorted or very nearly sorted.

# Frequently, pessimism is warranted. When there's a need to plan defensively about the cost of an algorithm, the worst-case analysis is the critical one.

# In many cases, the reality is expected to be something in between. That's where average-case analysis is called for.
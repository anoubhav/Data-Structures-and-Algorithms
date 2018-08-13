def merge(left, right):
    left_index = 0
    right_index = 0
    results = []
    while left_index<len(left) and right_index<len(right):
        if left[left_index]<right[right_index]:
            results.append(left[left_index])
            left_index += 1
        else:
            results.append(right[right_index])
            right_index += 1
    results.extend(left[left_index:])
    results.extend(right[right_index:])
    return results
def mergesort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
    return merge(left, right)

import random 
random_list = random.sample(range(1000), 100)
print(f'\nBefore sorting:\n{random_list}')
print(f'\nAfter sorting:\n{mergesort(random_list)}\n')

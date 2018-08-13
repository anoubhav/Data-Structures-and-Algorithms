import random 
random_list = random.sample(range(1000), 100)
print(f'Before sorting:{random_list}')
def insertion_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0,i):
            if arr[i-j] < arr[i-j-1]:
                arr[i-j], arr[i-j-1] = arr[i-j-1], arr[i-j]
            else:
                break
    return arr
print(f'\nAfter sorting:{insertion_sort(random_list)}')

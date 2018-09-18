arr = [i for i in range(10000000)]

def binary_search_iterative(search_elem, arr):
    len_arr = len(arr)
    start = 0
    end = len_arr - 1
    mid = (start + end)//2
    while mid!=start:
        if search_elem>arr[mid]:
            start = mid
            mid = (start + end)//2
        elif search_elem<arr[mid]:
            end = mid
            mid = (start + end)//2
        elif search_elem == arr[mid]:
            return True
    return False

def binary_search_recursive(search_elem ,arr):
    len_arr = len(arr)
    start = 0
    end = len_arr - 1
    mid = (start + end)//2
    def _binary_search_recursive(arr, start, mid, end):
        if mid == start:
            return False
        if search_elem>arr[mid]:
            start = mid
            mid = (start + end)//2
            return _binary_search_recursive(arr, start, mid, end)
        elif search_elem<arr[mid]:
            end = mid
            mid = (start + end)//2
            return _binary_search_recursive(arr, start, mid, end)
        elif search_elem == arr[mid]:
            return True
    return _binary_search_recursive(arr, start, mid, end)
        
def linear_search(search_elem, arr):
    for i in arr:
        if i == search_elem:
            return True
    return False

def binary_search_brilliant(A, item):
    if len(A) == 0:
        return False
    else:
        middle = len(A) // 2
        if A[middle] == item:
            return True
        if A[middle] > item:
            return binary_search_brilliant(A[:middle], item)
        else:
            return binary_search_brilliant(A[middle + 1:], item)

lst = [1, 2, 3, 5, 8, 22, 34, 42, 87, 103]
print(binary_search_brilliant(lst, 4))
print(binary_search_brilliant(lst, 42))
print('hi')
print(binary_search_iterative(99000000, arr))
print(binary_search_recursive(9900000, arr))
print(linear_search(99000, arr))
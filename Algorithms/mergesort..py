arr= [1, 4, 3, 2, 1, 8, 11, 0 ]

def merge(left, right):
    ans = []
    i, j = 0, 0
    for _ in range(len(left) + len(right)):
        if i<len(left) and j<len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1

    return ans + left[i:] + right[j:]
        
def mergesort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)


print(mergesort(arr))
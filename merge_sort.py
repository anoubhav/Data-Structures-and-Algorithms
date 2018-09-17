def create_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

def merge(a, b):
    c = [] # final output array
    a_idx, b_idx = 0, 0
    while a_idx<len(a) and b_idx<len(b):
        if a[a_idx]<b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
    if a_idx==len(a): c.extend(b[b_idx:])
    else: c.extend(a[a_idx:])
    return c

def mergesort(a):
    # a list of 0 or 1 element is sorted by definition
    if len(a)<=1: return a

    # split the list in half and call mergesort recursively for each half
    left, right = mergesort(a[:len(a)//2]), mergesort(a[len(a)//2:])

    # merge the now-sorted sublists
    return merge(left, right)

a = create_array()
print(a)
s = mergesort(a)
print(s)

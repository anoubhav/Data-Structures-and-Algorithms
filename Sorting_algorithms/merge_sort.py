def create_array(size=10, max=50):
    """ Returns random array of given size and elements upto max
    (int, int) -> (list) """
    from random import randint
    return [randint(0, max) for _ in range(size)]

def merge(a, b):
    """ Conquer routine(does all the work)"""
    c = [] # final output array
    a_idx, b_idx = 0, 0
    while a_idx<len(a) and b_idx<len(b):
        if a[a_idx]<b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
    # if a_idx==len(a): c.extend(b[b_idx:])
    # else: c.extend(a[a_idx:])
    c += a[a_idx:]
    c += b[b_idx:]
    return c

def merge_sort(a):
    """ Divide routine """
    # a list of 0 or 1 element is sorted by definition
    if len(a)<=1: return a

    # split the list in half and call merge_sort recursively for each half
    left, right = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])

    # merge the now-sorted sublists
    return merge(left, right)

def main():
    a = create_array()
    print(a)
    s = merge_sort(a)
    print(s)
    
if __name__ == '__main__':
    main()


""" The number of moves necessary to move n disks can be calculated as 2^n-1. Hence, exponential run time for the towers of hanoi """

def hanoi(n, from_rod, to_rod, aux_rod):
    if n<=0:
        raise ValueError('Invalid number of disks')
    if n == 1:
        print('Move disk 1 from rod', from_rod,'to rod',to_rod)
        return
    hanoi(n-1, from_rod, aux_rod, to_rod)
    print('Move disk', n, 'from rod', from_rod, 'to rod', to_rod)
    hanoi(n-1, aux_rod, to_rod, from_rod)
disks = input('\nEnter number of disks in the Tower of Hanoi:')
hanoi(int(disks),"A","C","B")
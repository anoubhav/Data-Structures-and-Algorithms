# longest increasing subsequence; O(n**2) implementation below. Can be O(nlogn)

# Find the length of the longest increasing subsequence in given array
sequence = [6,2,5,1,7,4,8,3]
n = len(sequence)
length = [1]*(n) # length of the LIS ending at n

for end in range(1, n):
    for prev in range(end):
        if sequence[prev] < sequence[end]:
            length[end] = max(length[end], length[prev] + 1)

print(max(length))




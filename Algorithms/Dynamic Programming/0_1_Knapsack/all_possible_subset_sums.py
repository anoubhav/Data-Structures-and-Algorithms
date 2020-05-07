## Knapsack problem
# Given a list of weights
# [w1,w2,...,wn], determine all sums that can be constructed using the weights

# To solve the problem, we focus on subproblems where we only use the first k
# weights to construct sums. Let possible(x, k) = true if we can construct a sum x
# using the first k weights, and otherwise possible(x, k) = false
w = [1, 3, 3, 5]
w = [0] + w
n = len(w)
maxsum = sum(w)


def two_dim_dp(w, n, maxsum):
    # SOLN: 1 Using a 2dimensional state vector possible[x][k] ; O(n*maxsum)
    possible = [[0]*n for _ in range(maxsum+1)]
    possible[0][0] = 1 # to form sum of 0 with 0 elements

    for k in range(1, n):
        for s in range(maxsum+1):
            disclude = possible[s][k-1]
            include  = possible[s-w[k]][k-1] if s-w[k]>=0 else 0
            possible[s][k] = disclude | include

    # Print the last column of possible[S][N], which gives the possibility of constructing a sum from 0.. S using N elements.
    print([row[n-1] for row in possible])

def one_dim_dp(w, n, maxsum):
    ## SOLN2: Using only a 1-dimensional state vector, possible[x] ; O(n*maxsum)
    # possible(x) checks if a subset of the w vector can be used to make x.
    possible = [0 for _ in range(maxsum+1)]
    possible[0] = 1

    for k in range(1, n):   
        for x in range(maxsum, -1, -1):
            if possible[x]:
                possible[x+w[k]] = 1
    print(possible)

two_dim_dp(w, n, maxsum)
one_dim_dp(w, n, maxsum)
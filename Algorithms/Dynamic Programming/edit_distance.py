## Edit distance or Levenshtein distance

# Suppose that we are given a string x of length n and a string y of length m,
# and we want to calculate the edit distance between x and y. To solve the problem,
# we define a function distance(a,b) that gives the edit distance between prefixes
# x[0...a] and y[0...b]. 

# distance(a, b) = min(distance(a, b-1) + 1, distance(a-1, b) + 1, distance(a-1, b-1) + 1 - int(x[a] == y[b]))

def edit_distance(x, y):
    m, n = len(x), len(y)

    # initialize
    distance = [[0]*(m+1) for _ in range(n+1)]

    # distance(a, 0) = a; i.e., the top row
    distance[0] = list(range(m+1))

    # distance(0, b) = b; i.e., the first column
    for i in range(n+1):
        distance[i][0] = i

    # Fill the DP matrix
    for a in range(1, n+1):
        for b in range(1, m+1):
            distance[a][b] = min(distance[a][b-1] + 1, distance[a-1][b] + 1, distance[a-1][b-1] + 1 - int(x[b-1] == y[a-1]))

    return (distance[n][m])

x = 'coow'
y = 'cowd'
print(edit_distance(x, y))
## Paths in grid; O(n^2)
values = [[3, 7, 9, 2, 7], [9, 8, 3, 5, 5], [1, 7, 9, 8, 5], [3, 8, 6, 4, 10], [6, 3, 9, 7, 8]]
m, n = len(values), len(values[0])
sumsf = [[0]*(n) for _ in range(m)]
sumsf[0][0] = values[0][0]

for x in range(m):
    for y in range(n):
        top = sumsf[x-1][y] if x>0 else 0
        left = sumsf[x][y-1] if y>0 else 0
        sumsf[x][y] = max(top, left) + values[x][y]

print(sumsf[m-1][n-1])
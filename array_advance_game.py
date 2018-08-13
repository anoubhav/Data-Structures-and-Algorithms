arr = [3, 2, 0, 0, 2, 0, 1]
furthest_reached = 0
for i in range(len(arr)):
    if i > furthest_reached:
        print('Not possible')
        exit()
    if furthest_reached > len(arr) - 1:
        break
    furthest_reached = max(furthest_reached, arr[i] + i)
print('Possible')
    


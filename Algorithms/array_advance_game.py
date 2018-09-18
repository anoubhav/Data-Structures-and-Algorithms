"""  In this game, you are given an array of non-negative integers. For example:[3,3,1,0,2,0,1].

Each number represents the maximum you can advance in the array. 

Question:
Is it possible to advance from the start of the array to the last element? """


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
    


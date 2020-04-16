t = int(input())
for _ in range(t):
    x, n, m = list(map(int, input().split()))

    # n -> x//2 + 10
    # m -> x - 10

    flag = 'NO'
    count = n+m
    for i in range(count):
        if n!=0:
            if x//2 +10 < x:
                x = x//2 +10
                n = n-1
            else:
                n = 0
        elif m!=0:
            x = x - 10
            m = m-1

        if x<=0:
            flag = 'YES'
            break
    
    print(flag)
    
    
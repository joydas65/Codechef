for _ in range(int(input())):
    
    x,y,n,r = map(int, input().split())
    
    if x*n > r:
        print(-1)
    elif y*n < r:
        print(0,n)
    else:
        premium_burgers = (r - (n*x)) // (y-x)
        print(n-premium_burgers,premium_burgers)

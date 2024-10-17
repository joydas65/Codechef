for _ in range(int(input())):
    
    n,m = map(int, input().split())
    
    print("No" if (n%2 == 1 and m%2 == 1) or (n == 1 or m == 1) else "Yes")

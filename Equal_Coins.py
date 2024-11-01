for _ in range(int(input())):
    
    x,y = map(int, input().split())
    
    if (x%2 == 0 and y%2 == 0) or (x > 0 and x%2 == 0 and y%2 == 1):
        print("YES")
    else:
        print("NO")

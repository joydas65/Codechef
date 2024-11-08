for _ in range(int(input())):
    
    n,x = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    flag = 0
    
    for i in arr:
        
        if i >= x:
            flag = 1
            break
        
    print("YES" if flag == 1 else "NO")

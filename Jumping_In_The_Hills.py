for _ in range(int(input())):
    
    n,u,d = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    i,c = 1,0
    
    while i < n:
        
        if arr[i] - arr[i-1] > u:
            break
        if arr[i-1] - arr[i] > d:
            if c >= 1:
                break
            c += 1
            
        i += 1
        
    print(i)

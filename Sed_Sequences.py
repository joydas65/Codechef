for _ in range(int(input())):
    
    n,k = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    s = 0
    
    for item in arr:
        
        s += item
        
    if s % k == 0:
        
        print(0)
        
    else:
        
        print(1)

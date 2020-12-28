for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    d,a,b,c = dict(),-1,-1,-1
    
    for item in arr:
        
        if item in d:
            
            d[item] += 1
            
            a = max(a, item)
            
            if d[item] >= 4:
                
                c = max(c, item)
            
        else:
            
            d[item] = 1
            
    for item in d:
        
        if item != a and d[item] >= 2:
            
            b = max(b, item)
            
    if a == -1 or b == -1:
        
        if c == -1:
        
            print(-1)
            
        else:
            
            print(c*c)
    else:
        
        print(max(a*b, c*c))

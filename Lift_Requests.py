for _ in range(int(input())):
    
    n,q = map(int, input().split())
    
    previousFloor,ans = 0,0
    
    for i in range(q):
        
        f,d = map(int, input().split())
        
        if i == 0:
            ans += f
        elif i > 0:
            ans += abs(f - previousFloor)
            
        ans += abs(f - d)
        #print(ans)
        previousFloor = d
        
    print(ans)
        

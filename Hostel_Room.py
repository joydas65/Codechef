for _ in range(int(input())):
    
    n,x = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    ans,currentCount = x,x
    
    for i in arr:
        
        currentCount += i
        
        ans = max(ans, currentCount)
        
    print(ans)

for _ in range(int(input())):
    
    n,d = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    risk = 0
    
    for i in arr:
        
        if i >= 80 or i <= 9:
            risk += 1
            
    ans = (n-risk)//d
    
    if (n-risk) % d != 0:
        ans += 1
        
    ans += (risk)//d
    
    print(ans+1 if risk % d != 0 else ans)

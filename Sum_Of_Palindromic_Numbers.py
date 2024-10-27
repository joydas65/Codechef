for _ in range(int(input())):
    
    n,m = map(int, input().split())
    
    ans,i = 0,n
    
    while i <= m:
        
        if str(i) == str(i)[::-1]:
            ans += i
            
        i += 1
        
    print(ans)

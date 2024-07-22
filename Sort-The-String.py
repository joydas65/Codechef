for _ in range(int(input())):
    
    n = int(input())
    
    s = input()
    
    ans = 0
    
    for i in range(n-1):
        
        if s[i] == '1' and s[i+1] == '0':
            ans += 1
            
    print(ans)

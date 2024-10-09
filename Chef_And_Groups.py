for _ in range(int(input())):
    
    s = input()
    ans,n,freq = 0,len(s),0
    
    for i in range(n):
        
        if s[i] == '1' and freq == 0:
            ans += 1
            freq += 1
        elif s[i] == '0':
            freq = 0
            
    print(ans)

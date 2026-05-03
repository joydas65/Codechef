for _ in range(int(input())):
    
    n = int(input())
    
    s = input()
    
    l,ans = len(s),0
    
    for i in range(1,l-1):
        if s[i] == '0' and not (s[i-1] == '1' or s[i+1] == '1'):
            ans += 1
            
    if s[0] == '0' and 1 < l and s[1] == '0':
        ans += 1
        
    if s[l-1] == '0' and l-2 >= 0 and s[l-2] == '0':
        ans += 1
        
    print(1 if l == 1 and s[0] == '0' else ans)

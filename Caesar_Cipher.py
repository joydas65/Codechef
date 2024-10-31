for _ in range(int(input())):
    
    n = int(input())
    
    s = input()
    t = input()
    u = input()
    
    k = 0
    
    c1,c2 = ord(s[0]),ord(t[0])
    
    if c2 >= c1:
        k = c2-c1
    else:
        k = c2 + 26 - c1
        
    ans = ''
    
    for i in u:
        
        if ord(i) + k > 122:
            ans += chr(ord(i) + k - 26)
        else:
            ans += chr(ord(i) + k)
        
    print(ans)

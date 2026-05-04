for _ in range(int(input())):
    
    st = input().split(' ')
    
    n,ans = len(st),''
    
    for i in range(n):
        
        if i == n-1:
            ans += st[i][0].upper() + st[i][1:]
        else:
            ans += st[i][0].upper() + ". "
    
    print(ans)

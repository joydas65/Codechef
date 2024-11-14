for _ in range(int(input())):
    
    s,n = map(int, input().split())
    
    ans = s//n
    
    if s%n > 0:
        if (s%n)%2 == 0 or (s%n) == 1:
            ans += 1
        elif (s%n) > 2:
            ans += 2
            
    print(ans)

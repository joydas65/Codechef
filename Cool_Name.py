for _ in range(int(input())):
    
    name = input()
    
    ans,idx = 0,1
    
    for c in "abcdefghijklmnopqrstuvwxyz":
        for i in name:
            if i == c:
                ans += (idx * (ord(c) - 96))
                idx += 1
        
    print(ans)

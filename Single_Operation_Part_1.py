for _ in range(int(input())):
    
    n = int(input())
    s = input()
    ans = n
    
    for i,j in enumerate(s):
        
        if j == '0':
            ans = i
            break
        
    print(ans)

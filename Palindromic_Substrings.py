for _ in range(int(input())):
    
    s1 = input()
    s2 = input()
    
    seen,flag = set(),0
    
    for i in s1:
        seen.add(i)
        
    for i in s2:
        if i in seen:
            flag = 1
            break
        
    print("Yes" if flag == 1 else "No")

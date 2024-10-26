for _ in range(int(input())):
    
    A = input()
    B = input()
    
    N = len(A)
    
    a0,a1,b0,b1 = 0,0,0,0
    
    for i in A:
        if i == '0':
            a0 += 1
        else:
            a1 += 1
            
    for i in B:
        if i == '0':
            b0 += 1
        else:
            b1 += 1
            
    ones = min(a0,b1) + min(a1,b0)
            
    print(('1' * ones) + ('0' * (N - ones))) 

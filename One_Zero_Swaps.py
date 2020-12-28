for _ in range(int(input())):
    
    n = int(input())
    
    s = input()
    
    p = input()
    
    zeroes1,ones1,zeroes2,ones2 = 0,0,0,0
    
    for i,j in enumerate(s):
        
        if j == '0':
            
            zeroes1 += 1
            
        else:
            
            ones1 += 1
            
        if p[i] == '0':
            
            zeroes2 += 1
            
        else:
            
            ones2 += 1
            
    if ones1 != ones2 or zeroes2 != zeroes1:
        
        print("No")
        
    else:
        
        c1,c2,f = 0,0,0
        
        for i,j in enumerate(s):
            
            if j == '1':
                
                c1 += 1
                
            if p[i] == '1':
                
                c2 += 1
                
            if c1 < c2:
                
                f = 1
                
                break
            
        print("No" if f == 1 else "Yes")

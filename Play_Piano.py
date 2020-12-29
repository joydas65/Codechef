# Question Link https://www.codechef.com/problems/PLAYPIAN

for _ in range(int(input())):
    
    s = input()
    
    f,i,n = 0,1,len(s)
    
    while i < n:
        
        if s[i] == s[i-1]:
            
            f = 1
            
            break
        
        i += 2
        
    print("no" if f == 1 else "yes")

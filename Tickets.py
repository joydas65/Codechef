# Question Link https://www.codechef.com/problems/TICKETS5

for _ in range(int(input())):
    
    s = input()
    
    n = len(s)
    
    if s[0] == s[1]:
        
        print("NO")
        
    else:
        
        i = 0
        
        while i+2 < n:
            
            if s[i] != s[i+2]:
                
                print("NO")
                
                break
            
            i += 1
            
        if i+2 >= n:
            
            print("YES")

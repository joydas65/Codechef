# Question Link https://www.codechef.com/problems/GIFTSRC

for _ in range(int(input())):
    
    n = int(input())
    
    s = input()
    
    f1,f2,x,y = 0,0,0,0
    
    for i in s:
        
        if i == 'L' or i == 'R':
            
            if f1 == 0:
                
                if i == 'L':
                    
                    x -= 1
                    
                else:
                    
                    x += 1
                    
            f1,f2 = 1,0
            
        elif i == 'D' or i == 'U':
            
            if f2 == 0:
                
                if i == 'D':
                    
                    y -= 1
                    
                else:
                    
                    y += 1
                    
            f2,f1 = 1,0
            
    print(x,y)

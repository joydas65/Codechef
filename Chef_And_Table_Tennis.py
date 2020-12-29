# Question Link https://www.codechef.com/problems/TTENIS

for _ in range(int(input())):
    
    s = input()
    
    one,zero = 0,0
    
    for i,j in enumerate(s):
        
        if j == '0':
            
            zero += 1
            
        else:
            
            one += 1
            
    print("WIN" if one > zero else "LOSE")

# Question Link https://www.codechef.com/problems/CV

for _ in range(int(input())):
    
    n = int(input())
    
    s = input()
    
    i,x,ans = 0,set(),0
    
    x.add('a')
    x.add('e')
    x.add('i')
    x.add('o')
    x.add('u')
    
    while i+1 < n:
            
        if s[i] not in x and s[i+1] in x:
            
            ans += 1
            
        i += 1
        
    print(ans)

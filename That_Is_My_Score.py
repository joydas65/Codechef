# Question Link https://www.codechef.com/problems/WATSCORE

for _ in range(int(input())):
    
    n = int(input())
    
    ans,d = 0,dict()
    
    for i in range(n):
        
        p,s = map(int, input().split())
        
        if p <= 8:
            
            if p in d:
                
                d[p] = max(d[p], s)
                
            else:
                
                d[p] = s
                
    for i in d:
        
        ans += d[i]
        
    print(ans)

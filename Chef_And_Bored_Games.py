# Question Link

# https://www.codechef.com/problems/PCJ18B

for _ in range(int(input())):
    
    n = int(input())
    
    ans = 0
    
    while n > 0:
        
        ans += (n*n)
        
        n -= 2
        
    print(ans)

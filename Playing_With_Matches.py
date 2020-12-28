d = dict()

d[0],d[1],d[2] = 6,2,5

d[3],d[4],d[5] = 5,4,5

d[6],d[7],d[8],d[9] = 6,3,7,6

for _ in range(int(input())):
    
    a,b = map(int, input().split())
    
    n,ans = a+b,0
    
    while n != 0:
        
        ans += d[n%10]
        
        n //= 10
        
    print(ans)

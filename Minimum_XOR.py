for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    xor,ans = 0,1000000
    
    for i in arr:
        
        xor ^= i
        
    for i in arr:
        
        ans = min(ans, xor ^ i, xor)
        
    print(ans)

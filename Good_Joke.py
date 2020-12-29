for _ in range(int(input())):
    
    n = int(input())
    
    arr = []
    
    for i in range(n):
        
        a,b = map(int, input().split())
        
        arr.append((a,b,i+1))
        
    arr,ans = sorted(arr),0
    
    for i,j in enumerate(arr):
        
        ans = ans ^ j[2]
            
    print(ans)

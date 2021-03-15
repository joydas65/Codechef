import sys

for _ in range(int(input())):
    
    n,k = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    if k == 1:
        
        print(0)
        
    else:
        
        arr,i,ans = sorted(arr),0,sys.maxsize
        
        while i+k <= n:
            
            ans = min(arr[i+k-1] - arr[i], ans)
            
            i += 1
            
        print(ans)

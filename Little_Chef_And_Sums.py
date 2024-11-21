for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    prefix = [arr[0]]
    
    for i in range(1,n):
        prefix.append(prefix[-1] + arr[i])
        
    suffix = [0 for i in range(n)]
    suffix[n-1] = arr[n-1]
    minValue,ans = float("inf"),float("inf")
    
    for i in range(n-2,-1,-1):
        
        suffix[i] += (suffix[i+1] + arr[i])
        
    for i in range(n):
        if prefix[i]+suffix[i] < minValue:
            minValue = prefix[i]+suffix[i]
            ans = i+1
            
    #print(prefix,suffix)
            
    print(ans)

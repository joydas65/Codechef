for _ in range(int(input())):
    
    n,k = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    weight,i,ans = 0,0,0
    
    while i < n:
        
        if arr[i] > k:
            break
        else:
            if weight + arr[i] <= k:
                weight += arr[i]
            else:
                ans += 1
                weight = arr[i]
        i += 1
        
    print(-1 if i < n else ans+1)

for _ in range(int(input())):
    
    n,k = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    d,disqualify,ans = dict(),set(),0
    
    for i in range(n):
        
        if i+1 == arr[i]:
            if i+1 in d:
                del d[i+1]
            disqualify.add(arr[i])
        elif arr[i] not in disqualify:
            if arr[i] in d:
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
                
    for i in d:
        if d[i] >= k:
            ans += 1
            
    print(ans)

for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    d,mx,ans = dict(),0,float('inf')
    
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        
    freq = dict()
    
    for i in d:
        if d[i] in freq:
            freq[d[i]] += 1
        else:
            freq[d[i]] = 1
            
        mx = max(mx, freq[d[i]])
        
    #print(freq,mx)
    
    for i in freq:
        if mx == freq[i]:
            ans = min(ans, i)
            
    print(ans)

for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    d,freq,mx = dict(),0,100000
    
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
            
        freq = max(freq, d[i])
            
    for i in d:
        if freq == d[i]:
            mx = min(mx, i)
            
    print(mx, freq)

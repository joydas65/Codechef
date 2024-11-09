for _ in range(int(input())):
    
    n = int(input())
    
    w = list(map(int, input().split()))
    
    i,mx = n - 1,0
    
    while i >= 0:
        if w[i] + i >= w[i]:
            mx = max(mx, w[i] + i)
        i -= 1
    
    print(mx)

for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    seen,ans = set(),0
    
    for i in arr:
        if i not in seen:
            seen.add(i)
        else:
            seen.remove(i)
        ans = max(ans, len(seen))
        
    print(ans)

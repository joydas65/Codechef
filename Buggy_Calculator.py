# Question Link https://www.codechef.com/problems/BUGCAL

for _ in range(int(input())):
    
    a,b = map(str, input().split())
    
    a,b = a[::-1],b[::-1]
    
    n,m = len(a),len(b)
    
    i,j,ans = 0,0,""
    
    while i < n and j < m:
        
        ans = str((ord(a[i]) + ord(b[j]) - 96) % 10) + ans
        
        i += 1
        
        j += 1
        
    if i >= n and j < m:
        
        while j < m:
            
            ans = b[j] + ans
            
            j += 1
            
    elif j >= m and i < n:
        
        while i < n:
            
            ans = a[i] + ans
            
            i += 1
            
    print(int(ans))

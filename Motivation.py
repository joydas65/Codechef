for _ in range(int(input())):
    
    n,x = map(int, input().split())
    
    arr = []
    
    for i in range(n):
        
        s,r = map(int, input().split())
        
        arr.append([s,r])
        
    arr = sorted(arr, key = lambda x : x[1], reverse = True)
    
    ans = -1
    
    for item in arr:
        
        if x >= item[0]:
            
            ans = item[1]
            
            break
        
    print(ans)

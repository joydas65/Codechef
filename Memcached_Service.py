for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(str, input().split()))
    
    flag,ans = 0,200
    
    for i in arr:
        
        if flag == 0 and i == "stop":
            
            ans = 404
            
            break
        
        elif flag == 0 and (i == "start" or i == "restart"):
            
            flag = 1
            
        elif flag == 1 and i == "stop":
            
            flag = 0
            
    print(ans)

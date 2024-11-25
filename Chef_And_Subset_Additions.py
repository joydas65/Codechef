for _ in range(int(input())):
    
    n,x,y = map(int, input().split())
    
    arrA = list(map(int, input().split()))
    
    arrB = list(map(int, input().split()))
    flag = 0
    
    for i in range(n):
        
        diff = arrB[i] - arrA[i]
        
        if not (diff == x or diff == y):
            flag = 1
            break
        
    print("Yes" if flag == 0 else "No")

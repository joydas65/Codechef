for _ in range(int(input())):
    
    n = int(input())
    
    arr = [0 for i in range(n)]
    
    arr[-1] = n
    arr[-2] = 1
    
    i = n-3
    
    while i >= 0:
        if i%2 == 1:
            if n%2 == 1:
                arr[i] = abs((i+1)-arr[i+1])
            else:
                arr[i] = (i+1)+arr[i+1]
        else:
            if n%2 == 0:
                arr[i] = abs((i+1)-arr[i+1])
            else:
                arr[i] = (i+1)+arr[i+1]
            
        i -= 1
        
    for i in arr:
        print(i,end=" ")
    print()

for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    i,j = 0,n-1
    
    while i < j:
        print(arr[i],end = " ")
        print(arr[j],end = " ")
        i += 1
        j -= 1
        
    if n % 2 == 1:
        print(arr[i])
    else:
        print()

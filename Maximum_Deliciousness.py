for _ in range(int(input())):
    
    n,k,l = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    arr = arr[::-1]
    result = 0
    
    for i in range(l-1,n,k):
        result += arr[i]
        
    print(result)

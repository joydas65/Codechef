for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    sumA = sum(arr)//(n+1)
    
    for i in arr:
        print(i-sumA,end=" ")
    print()

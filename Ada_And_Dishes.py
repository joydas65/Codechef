for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    if n <= 2:
        print(max(arr))
    elif n == 3:
        print(max(arr[-1],arr[0]+arr[1]))
    else:
        print(min(max(arr[-1]+arr[0],arr[1]+arr[2]),max(arr[-1],arr[0]+arr[1]+arr[2])))

for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    totalSum = sum(arr)
    
    avg = totalSum/n
    
    ans = "Impossible"
    
    for i,num in enumerate(arr):
        
        if ((totalSum - num) / (n - 1)) == avg:
            ans = i+1
            break
        
    print(ans)

for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    ans = 0
    
    for i in range(n):
        
        if arr[i] == (i + 1 + ans):
            ans += 1
            
    print(ans)

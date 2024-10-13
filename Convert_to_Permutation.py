for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    arr.sort()
    ans,flag = 0,0
    
    for i,j in enumerate(arr):
        if j > i+1:
            flag = 1
            break
        else:
            ans += abs(j-i-1)
            
    print(-1 if flag == 1 else ans)

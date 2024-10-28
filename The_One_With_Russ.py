for _ in range(int(input())):
    
    n,x,k = map(int, input().split())
    
    arrA = list(map(int, input().split()))
    
    arrB = list(map(int, input().split()))
    
    ans = 0
    
    for i,j in enumerate(arrA):
        
        if abs(j - arrB[i]) <= k:
            ans += 1
            
        if ans == x:
            break
            
    print("YES" if ans == x else "NO")

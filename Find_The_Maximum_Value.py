# Question Link https://www.codechef.com/problems/LOSTMAX

for _ in range(int(input())):
    
    arr = list(map(int, input().split()))
    
    n,ans = len(arr),-1
    
    v = arr.index(n-1)
    
    for i,item in enumerate(arr):
        
        if i != v:
            
            ans = max(ans, item)
            
    print(ans)

# Question Link https://www.codechef.com/problems/PRGIFT

for _ in range(int(input())):
    
    n,K = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    flag = 0
    
    for i in range(n):
        
        for j in range(i,n):
            
            c = 0
            
            for k in range(i,j+1):
                
                if arr[k] % 2 == 0:
                    
                    c += 1
                    
            if c == K:
                
                flag = 1
                
                break
            
    print("YES" if flag == 1 else "NO")

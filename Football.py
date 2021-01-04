# Question Link https://www.codechef.com/problems/MSNSADM1

for _ in range(int(input())):
    
    n = int(input())
    
    arrA = list(map(int, input().split()))
    
    arrB = list(map(int, input().split()))
    
    m,ans = 0,-1
    
    for i,j in enumerate(arrA):
        
        m = max(m, (j*20) - (arrB[i]*10))
        
    print(m)

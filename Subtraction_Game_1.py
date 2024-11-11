def findGCD(a, b):
    
    if a % b == 0:
        return b
        
    return findGCD(b, a % b)

for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    gcd = arr[0]
    
    for i in range(1,n):
        
        gcd = findGCD(gcd, arr[i])
        
    print(gcd)

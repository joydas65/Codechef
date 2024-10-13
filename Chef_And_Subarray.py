n = int(input())
    
arr = list(map(int, input().split()))

product,ans,c = 1,0,0

for i in arr:
    product *= i
    
    if product > 0:
        c += 1
        ans = max(ans, c)
    else:
        product,c = 1,0
        
print(ans)

prime = [True for i in range(3001)]
p = 2

while p*p <= 3000:
    if prime[p] == True:
        for i in range(p*p, 3001, p):
            prime[i] = False
    p += 1


for _ in range(int(input())):
    
    x,y = map(int, input().split())
    
    i = x+y+1
    
    while i <= 3000:
        if prime[i] == True:
            break
        i += 1
        
    print(i-x-y)

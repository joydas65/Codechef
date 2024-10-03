import math

for _ in range(int(input())):
    
    n,a = map(int, input().split())
    
    print(int(math.floor(math.sqrt(n))) * a)

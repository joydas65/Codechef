for _ in range(int(input())):
    
    a,b = map(int, input().split())
    
    oddA = (a+1)//2
    evenA = a - oddA
    
    oddB = (b + 1)//2
    evenB = b - oddB
    
    print((oddB*oddA) + (evenB*evenA))

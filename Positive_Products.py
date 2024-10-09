for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    positive,negative = 0,0
    
    for i in arr:
        
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
            
    print(((positive*(positive-1))//2) + (negative*(negative-1))//2)

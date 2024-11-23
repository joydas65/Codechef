for _ in range(int(input())):
    
    n = int(input())
    
    ans = 0
    
    for x in range(n):
        
        price,quantity,discount = map(int, input().split())
        
        initialPrice = price + (price * discount)/100
        
        priceAfterDiscount = initialPrice - (initialPrice*discount)/100
        
        if priceAfterDiscount <= initialPrice:
            ans += (quantity * abs(priceAfterDiscount - price))
    
    print(ans)

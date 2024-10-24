for _ in range(int(input())):
    
    n,s = map(int, input().split())
    
    prices = list(map(int, input().split()))
    
    players = list(map(int, input().split()))
    
    lowestDefenderPrice,lowestForwardPrice = 1000,1000
    
    for i,j in enumerate(players):
        
        if j == 0:
            lowestDefenderPrice = min(lowestDefenderPrice, prices[i])
        elif j == 1:
            lowestForwardPrice = min(lowestForwardPrice, prices[i])
            
    if lowestDefenderPrice == 1000 or lowestForwardPrice == 1000:
        print("no")
    elif s + lowestDefenderPrice + lowestForwardPrice > 100:
        print("no")
    else:
        print("yes")
        
    #print(lowestDefenderPrice,lowestForwardPrice)

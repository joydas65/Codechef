for _ in range(int(input())):
    
    word1 = input()
    word2 = input()
    
    d,ans = dict(),0
    
    for c in word1:
        
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
            
    for c in word2:
        if c in d and d[c] > 0:
            ans += 1
            d[c] -= 1
            
    print(ans)

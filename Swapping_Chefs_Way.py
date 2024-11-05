for _ in range(int(input())):
    
    n = int(input())
    
    word = list(input())
    
    i,flag,j = 0,0,n-1
    
    while i < j:
        
        if ord(word[j]) < ord(word[i]):
            word[i],word[j] = word[j],word[i]
            
        i += 1
        j -= 1
        
    i = 0
    
    while i < n-1:
        if ord(word[i]) > ord(word[i+1]):
            flag = 1
            break
        
        i += 1
        
    print("YES" if flag == 0 else "NO")

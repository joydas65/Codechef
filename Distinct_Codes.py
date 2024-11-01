for _ in range(int(input())):
    
    word = input()
    
    n,seen = len(word),set()
    
    for i in range(n-1):
        seen.add(word[i]+word[i+1])
        
    print(len(seen))

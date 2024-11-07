mod = 1000000007

consonants = {'c', 'g', 'l', 'r'}

for _ in range(int(input())):
    
    n = int(input())
    
    word = input()
    c = 0
    
    for i in word:
        if i in consonants:
            c += 1
            
    print((2**c) % mod)

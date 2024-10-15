for _ in range(int(input())):
    
    n = int(input())
    
    d = dict()
    d['c'] = 0
    d['o'] = 0
    d['d'] = 0
    d['e'] = 0
    d['h'] = 0
    d['f'] = 0
    
    for i in range(n):
        
        s = input()
        
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
                
    d['c'] //= 2
    d['e'] //= 2
                
    ans = 2000
    for i in ['c', 'o', 'd', 'e', 'h', 'f']:
        ans = min(ans, d[i])
        
    print(ans)
    

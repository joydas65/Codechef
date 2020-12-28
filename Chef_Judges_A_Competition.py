for _ in range(int(input())):
    
    n = int(input())
    
    alice = list(map(int, input().split()))
    
    bob = list(map(int, input().split()))
    
    s1,s2,m1,m2 = 0,0,0,0
    
    for i,j in enumerate(alice):
        
        s1 += j
        
        s2 += bob[i]
        
        m1,m2 = max(m1, j),max(m2, bob[i])
        
    print("Alice" if s1-m1 < s2-m2 else "Bob" if s2-m2 < s1-m1 else "Draw")

for _ in range(int(input())):
    
    u,v,a,s = map(int, input().split())
        
    print("Yes" if (v*v) >= (u*u) - (2*a*s) else "No")

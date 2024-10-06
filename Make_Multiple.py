for _ in range(int(input())):
    
    a,b = map(int, input().split())
    
    print("YES" if b-a == 0 or a <= (b-a) else "NO")

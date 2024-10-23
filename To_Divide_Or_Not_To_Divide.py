for _ in range(int(input())):
    
    a,b,n = map(int, input().split())
    
    if a == b or a % b == 0:
        print(-1)
    else:
        if n % a == 0 and n % b != 0:
            print(n)
        else:
            n = ((n // a) + 1) * a
            
            while True:
                if n % a == 0 and n % b != 0:
                    print(n)
                    break
                n += a

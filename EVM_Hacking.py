for _ in range(int(input())):
    
    a,b,c,p,q,r = map(int, input().split())
    
    margin = (p+q+r)//2
    
    if p+b+c > margin or a+q+c > margin or a+b+r > margin or a+b+c > margin:
        print("YES")
    else:
        print("NO")

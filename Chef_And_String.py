for _ in range(int(input())):
    
    s = input()
    
    if s[1:] + s[0] == s[-1] + s[:-1]:
        print("YES")
    else:
        print("NO")

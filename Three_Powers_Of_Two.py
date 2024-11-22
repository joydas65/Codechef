for _ in range(int(input())):
    
    n = int(input())
    
    S = input()
    
    count = 0
    
    for i in S:
        if i == '1':
            count += 1
            
    if count >= 4:
        print("NO")
    elif count == 3 or count == 2 or (count == 1 and len(S) >= 3):
        print("YES")
    else:
        print("NO")

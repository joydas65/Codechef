for _ in range(int(input())):
    
    n,p = map(int, input().split())
    
    problems = list(map(int, input().split()))
    
    hard,cakewalk = 0,0
    
    for i in problems:
        
        if i <= p//10:
            hard += 1
        elif i >= p//2:
            cakewalk += 1
            
    print("yes" if cakewalk == 1 and hard == 2 else "no")

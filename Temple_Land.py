# Question Link https://www.codechef.com/problems/TEMPLELA

for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    flag = 0
    
    for i in range(n//2):
        
        if arr[i] != (i+1):
            
            flag = 1
            
            break
        
    if flag == 1:
        
        print("no")
        
    else:
        
        i,v = (n//2),(n//2)+1
        
        while i < n:
            
            if arr[i] != v:
                
                flag = 1
                
                break
            
            i += 1
            
            v -= 1
            
        if flag == 1 or v > 0:
            
            print("no")
            
        else:
            
            print("yes")

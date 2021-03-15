def findMinute(t):
    
    v = int(t[0]+t[1])%12
    
    if t[-2]+t[-1] == "PM":
        
        v += 12
        
    return (v*60) + int(t[3]+t[4])

for _ in range(int(input())):
    
    time = input()
    
    min1 = findMinute(time)
    
    n = int(input())
    
    ans = ""
    
    for i in range(n):
        
        x = input()
        
        min2 = findMinute(x[:8])
        
        min3 = findMinute(x[9:])
        
        if min2 <= min1 and min1 <= min3:
            
            ans += "1"
            
        else:
            
            ans += "0"
            
    print(ans)

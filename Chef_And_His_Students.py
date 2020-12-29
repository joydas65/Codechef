# Below is the question link

# https://www.codechef.com/problems/CHEFSTUD

for _ in range(int(input())):
    
    s = input()
    
    ans = 0
    
    for i,j in enumerate(s):
        
        if i >= 1:
            
            if j == '>' and s[i-1] == '<':
                
                ans += 1
                
    print(ans)

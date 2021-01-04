# Question Link https://www.codechef.com/problems/BRACKETS

for _ in range(int(input())):
    
    s = input()
    
    balance,maxBalance = 0,0
    
    for i in s:
        
        if i == '(':
            
            balance += 1
            
        elif i == ')':
            
            balance -= 1
            
        maxBalance = max(maxBalance, balance)
        
    print(("("*maxBalance) + (")"*maxBalance))

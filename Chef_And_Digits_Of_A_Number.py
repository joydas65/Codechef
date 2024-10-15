for _ in range(int(input())):
    
    s = input()
    
    count0,count1 = 0,0
    
    for i in s:
        
        if ord(i)-48 == 1:
            count1 += 1
        else:
            count0 += 1
            
    if count0 == 1 or count1 == 1:
        print("Yes")
    else:
        print("No")

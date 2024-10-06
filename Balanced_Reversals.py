for _ in range(int(input())):
    
    n = int(input())
    
    word = input()
    count0,count1 = 0,0
    
    for i in word:
        if i == '0':
            count0 += 1
        else:
            count1 += 1
            
    print(('0' * count0) + ('1' * count1))

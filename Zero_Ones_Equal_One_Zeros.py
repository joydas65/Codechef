for _ in range(int(input())):
    
    n = int(input())
    
    if n % 2 == 0:
        
        print("1" + ("0" * (n - 2)) + "1")
        
    else:
        
        zeroes = "0" * ((n - 1) // 2)
        
        print(zeroes + "1" + zeroes)

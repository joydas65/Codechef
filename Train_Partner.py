for _ in range(int(input())):
    
    n = int(input())
    
    if n % 8 == 7 or n % 8 == 0:
        print(str(n+1) + "SU" if n%8 == 7 else str(n-1) + "SL")
    elif n % 8 == 2 or n % 8 == 5:
        print(str(n+3) + "MB" if n%8 == 2 else str(n-3) + "MB")
    elif n % 8 == 1 or n % 8 == 4:
        print(str(n+3) + "LB" if n%8 == 1 else str(n-3) + "LB")
    elif n % 8 == 3 or n % 8 == 6:
        print(str(n+3) + "UB" if n%8 == 3 else str(n-3) + "UB")

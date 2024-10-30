arr = [1]
for i in range(100):
    arr.append(arr[-1] + 2)

for _ in range(int(input())):
    
    n = int(input())
    
    for i in range(n):
        print(arr[i],end = " ")
    print()

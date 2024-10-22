factorials = [1]

for i in range(1, 12):
    factorials.append(factorials[-1] * i)

def isSeatFree(seat):
    return 1 if seat == '0' else 0

x,n = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(input()))
    
front_seat,rear_seat,ans = 0,53,0
    
for i in range(n):
    front_seat,rear_seat = 0,53
    for j in range(9):
        free_seats = 0
        free_seats += isSeatFree(arr[i][front_seat])
        free_seats += isSeatFree(arr[i][front_seat + 1])
        free_seats += isSeatFree(arr[i][front_seat + 2])
        free_seats += isSeatFree(arr[i][front_seat + 3])
        free_seats += isSeatFree(arr[i][rear_seat])
        free_seats += isSeatFree(arr[i][rear_seat - 1])
        
        front_seat += 4
        rear_seat -= 2
        
        if free_seats >= x:
            ans += factorials[free_seats] // (factorials[x] * factorials[free_seats - x])
        
print(ans)

d,floor = dict(),1

for i in range(1,101):
    
    d[i] = floor
    
    if i % 10 == 0:
        
        floor += 1

for _ in range(int(input())):
    
    chef_room,chefina_room = map(int, input().split())
    
    print(abs(d[chef_room] - d[chefina_room]))

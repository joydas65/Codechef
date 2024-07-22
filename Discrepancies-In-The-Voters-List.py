n1,n2,n3 = map(int, input().split())

d = dict()

for i in range(n1):
    
    n = int(input())
    
    if n in d:
        d[n] += 1
    else:
        d[n] = 1
        
for i in range(n2):
    
    n = int(input())
    
    if n in d:
        d[n] += 1
    else:
        d[n] = 1
        
for i in range(n3):
    
    n = int(input())
    
    if n in d:
        d[n] += 1
    else:
        d[n] = 1
        
final_list = []

for i in d:
    
    if d[i] >= 2:
        
        final_list.append(i)
        
final_list = sorted(final_list)

print(len(final_list))

for i in final_list:
    
    print(i)

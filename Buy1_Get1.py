from collections import Counter

for _ in range(int(input())):
    
    d = Counter(input().strip())
    
    ans = 0
    for i in d.values():
        ans += (i + 1)//2
            
    print(ans)

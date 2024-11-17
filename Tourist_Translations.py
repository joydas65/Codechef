t,m = map(str, input().split())

mapper = {}

for i in range(97,123):
    mapper[chr(i)] = m[i-97]
    mapper[chr(i-32)] = chr(ord(m[i-97]) - 32)


for _ in range(int(t)):
    
    sentence = input()
    ans = ''
    
    for i in sentence:
        if i == '_':
            ans += ' '
        elif i in mapper:
            ans += mapper[i]
        else:
            ans += i
            
    print(ans)

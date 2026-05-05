import sys
input = sys.stdin.readline

T = int(input())
out = []
for _ in range(T):
    N = int(input())
    a = (N // 7) * 7
    while a >= 0:
        if (N - a) % 4 == 0:
            out.append(str(a))
            break
        a -= 7
    else:
        out.append("-1")
print('\n'.join(out))

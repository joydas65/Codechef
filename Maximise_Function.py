import sys
input = sys.stdin.readline

T = int(input())
out = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    out.append(str(2 * (max(A) - min(A))))
print('\n'.join(out))

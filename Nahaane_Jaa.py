import sys
input = sys.stdin.readline

T = int(input())
out = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if N == 1:
        out.append("Yes" if A[0] == K else "No")
    else:
        out.append("Yes" if K in A[:-1] else "No")
print("\n".join(out))

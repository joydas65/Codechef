import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
out = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    f = max(Counter(A).values())
    out.append("Yes" if 2 * f - 1 <= N else "No")
print("\n".join(out))

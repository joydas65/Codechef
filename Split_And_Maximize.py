import sys
input = sys.stdin.readline

MOD = 998244353
T = int(input())
out = []
for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    S = sum(C) % MOD
    ans = (S * S - S) % MOD
    out.append(str(ans))
print('\n'.join(out))

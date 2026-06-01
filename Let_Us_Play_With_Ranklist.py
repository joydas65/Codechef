import sys
input = sys.stdin.readline

def min_operations(n, s):
    for k in range(0, n + 1):
        kept = n - k
        lo = kept * (kept + 1) // 2   # sum if kept elements form {1..n-k}
        # k changed elements each in [1, n]: total addable in [k, k*n]
        if lo + k <= s <= lo + k * n:
            return k
    return n

T = int(input())
output = []
for _ in range(T):
    n, s = map(int, input().split())
    output.append(str(min_operations(n, s)))

sys.stdout.write('\n'.join(output) + '\n')

import sys
input = sys.stdin.readline

def construct(X):
    A = X | (1 << 27)
    B = X | (1 << 28)
    C = X | (1 << 29)
    return A, B, C

T = int(input())
out = []
for _ in range(T):
    X = int(input())
    A, B, C = construct(X)
    out.append(f"{A} {B} {C}")

sys.stdout.write('\n'.join(out) + '\n')

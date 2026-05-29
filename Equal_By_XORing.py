import sys
input = sys.stdin.readline

def min_xor_operations(A, B, N):
    D = A ^ B
    if D == 0:
        return 0

    high = (N - 1).bit_length()   # usable bit positions: 0 .. high-1
    if D >= (1 << high):          # D has a bit that no X (< N) can flip
        return -1

    if 1 <= D < N:                # single X = D works
        return 1
    return 2                      # feasible, needs two operations

T = int(input())
output = []
for _ in range(T):
    A, B, N = map(int, input().split())
    output.append(str(min_xor_operations(A, B, N)))

sys.stdout.write('\n'.join(output) + '\n')

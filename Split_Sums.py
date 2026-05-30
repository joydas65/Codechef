import sys
from math import gcd
input = sys.stdin.readline

def can_split(N, M):
    S = N * (N + 1) // 2

    if M > S:
        return False
    if (S + M) % 2 != 0:    # sums must be integers
        return False

    sumA = (S + M) // 2
    sumB = (S - M) // 2

    # gcd condition (handles empty-set case: gcd(0, k) = k)
    return gcd(sumA, sumB) == 1

T = int(input())
output = []
for _ in range(T):
    N, M = map(int, input().split())
    output.append("Yes" if can_split(N, M) else "No")

sys.stdout.write('\n'.join(output) + '\n')

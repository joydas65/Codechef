import sys
from math import gcd
input = sys.stdin.readline


def reconstruct_array(prefix_gcds):
    A = [prefix_gcds[0]]
    for i in range(1, len(prefix_gcds)):
        if prefix_gcds[i - 1] % prefix_gcds[i] != 0:
            return None
        A.append(prefix_gcds[i])
    return A


T = int(input())
output = []
for _ in range(T):
    N = int(input())
    B = list(map(int, input().split()))
    A = reconstruct_array(B)
    if A is None:
        output.append("-1")
    else:
        output.append(" ".join(map(str, A)))

sys.stdout.write("\n".join(output) + "\n")

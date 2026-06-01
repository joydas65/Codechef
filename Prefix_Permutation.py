import sys
input = sys.stdin.readline

def build_prefix_permutation(N, A):
    result = []
    prev = 0
    for marker in A:
        # Block covers values (prev+1 .. marker), placed in descending order
        result.extend(range(marker, prev, -1))
        prev = marker
    return result

T = int(input())
output = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    perm = build_prefix_permutation(N, A)
    output.append(' '.join(map(str, perm)))

sys.stdout.write('\n'.join(output) + '\n')

import sys
input = sys.stdin.readline

def max_total_child_height(A, B):
    total = sum(A) + sum(B)
    odd_A = sum(1 for x in A if x & 1)
    odd_B = sum(1 for x in B if x & 1)
    # Minimum odd-sum (parity-mismatched) pairs forced
    min_odd_pairs = abs(odd_A - odd_B)
    return (total - min_odd_pairs) // 2

T = int(input())
output = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    output.append(str(max_total_child_height(A, B)))

sys.stdout.write('\n'.join(output) + '\n')

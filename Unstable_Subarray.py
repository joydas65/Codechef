import sys
from collections import Counter
input = sys.stdin.readline

def count_unstable_subarrays(A):
    n = len(A)
    total_pairs = n * (n - 1) // 2          # all (l, r) with l < r

    # Subtract pairs with equal endpoints (those are stable)
    equal_endpoint_pairs = 0
    for freq in Counter(A).values():
        equal_endpoint_pairs += freq * (freq - 1) // 2

    return total_pairs - equal_endpoint_pairs

T = int(input())
output = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    output.append(str(count_unstable_subarrays(A)))

sys.stdout.write('\n'.join(output) + '\n')

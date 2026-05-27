import sys
input = sys.stdin.readline

def can_partition_into_odd_sum_subsets(N, K):
    # Each subset needs >= 2 elements
    if N < 2 * K:
        return False
    
    total_sum = N * (N + 1) // 2
    # Sum of K odd numbers has same parity as K
    if total_sum % 2 != K % 2:
        return False
    
    return True

T = int(input())
output = []
for _ in range(T):
    N, K = map(int, input().split())
    output.append("YES" if can_partition_into_odd_sum_subsets(N, K) else "NO")

sys.stdout.write('\n'.join(output) + '\n')

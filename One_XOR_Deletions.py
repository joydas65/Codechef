import sys
from collections import Counter
input = sys.stdin.readline

def min_deletions(arr):
    # Group by value with lowest bit cleared (x >> 1)
    # Each valid final array uses values from one such group {2k, 2k+1}
    group_counts = Counter(x >> 1 for x in arr)
    largest_group = max(group_counts.values())
    return len(arr) - largest_group

T = int(input())
output = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    output.append(str(min_deletions(A)))

sys.stdout.write('\n'.join(output) + '\n')

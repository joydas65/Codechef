import sys
input = sys.stdin.readline

def construct_alternating_divisibility_array(n):
    # Generate pairs (1,2), (3,6), (5,10), ...
    # Flatten and take first n elements
    result = []
    odd = 1
    while len(result) < n:
        result.append(odd)          # odd position element: 2k-1
        if len(result) < n:
            result.append(2 * odd)  # even position element: 2*(2k-1)
        odd += 2
    return result

T = int(input())
output_parts = []
for _ in range(T):
    N = int(input())
    arr = construct_alternating_divisibility_array(N)
    output_parts.append(' '.join(map(str, arr)))

sys.stdout.write('\n'.join(output_parts) + '\n')

import sys
input = sys.stdin.readline

def construct_n_plus_1_values(N):
    # Special case: N=1 needs exactly 2 values summing to 2, one repeated
    # Only valid answer: 1 1
    if N == 1:
        return [1, 1]

    # General case: 1, 2, ..., N-1, N-1, last_value
    # last_value = 2^N - sum(1..N-1) - (N-1)
    target_sum = 1 << N  # 2^N

    prefix_values = list(range(1, N))   # 1, 2, ..., N-1
    repeated_value = N - 1              # N-1 appears twice

    sum_so_far = sum(prefix_values) + repeated_value
    last_value = target_sum - sum_so_far

    return prefix_values + [repeated_value, last_value]

T = int(input())
output = []
for _ in range(T):
    N = int(input())
    values = construct_n_plus_1_values(N)
    output.append(' '.join(map(str, values)))

sys.stdout.write('\n'.join(output) + '\n')

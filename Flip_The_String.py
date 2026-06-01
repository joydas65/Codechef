import sys
input = sys.stdin.readline

def count_mismatch_blocks_by_parity(A, B):
    total_ops = 0
    # Process even and odd global indices independently
    for parity in (0, 1):
        in_block = False
        i = parity
        while i < len(A):
            mismatch = (A[i] != B[i])
            if mismatch and not in_block:
                total_ops += 1   # start of a new mismatch block
                in_block = True
            elif not mismatch:
                in_block = False
            i += 2
    return total_ops

T = int(input())
output = []
for _ in range(T):
    A = input().strip()
    B = input().strip()
    output.append(str(count_mismatch_blocks_by_parity(A, B)))

sys.stdout.write('\n'.join(output) + '\n')

import sys
input = sys.stdin.readline

def find_ordering_X(A, B, C):
    d_AB = (A ^ B).bit_length() - 1   # MSB position where A and B differ
    d_BC = (B ^ C).bit_length() - 1   # MSB position where B and C differ

    if d_AB == d_BC:
        return -1

    # Set bit d_AB to A's value  → forces (A⊕X) < (B⊕X)
    # Set bit d_BC to B's value  → forces (B⊕X) < (C⊕X)
    X = (A & (1 << d_AB)) | (B & (1 << d_BC))
    return X

T = int(input())
results = []
for _ in range(T):
    A, B, C = map(int, input().split())
    results.append(str(find_ordering_X(A, B, C)))

sys.stdout.write('\n'.join(results) + '\n')

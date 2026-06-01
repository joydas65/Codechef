import sys
input = sys.stdin.readline

def can_catch_thief(x, y, K, N):
    # Must be in the same residue class mod K
    if (x - y) % K != 0:
        return "No"
    # Gap measured in K-steps must be even
    gap_in_steps = abs(x - y) // K
    return "Yes" if gap_in_steps % 2 == 0 else "No"

T = int(input())
output = []
for _ in range(T):
    x, y, K, N = map(int, input().split())
    output.append(can_catch_thief(x, y, K, N))

sys.stdout.write('\n'.join(output) + '\n')

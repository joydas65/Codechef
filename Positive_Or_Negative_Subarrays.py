import sys
input = sys.stdin.readline

def positive_minus_negative_subarrays(B):
    P = 0  # sum of (position) where B_i = +1
    Q = 0  # sum of (position) where B_i = -1
    for index, b in enumerate(B, start=1):
        # 'index' subarrays end at this position, all sharing sign of b
        if b == 1:
            P += index
        else:
            Q += index
    return abs(P - Q)

T = int(input())
output = []
for _ in range(T):
    N = int(input())
    B = list(map(int, input().split()))
    output.append(str(positive_minus_negative_subarrays(B)))

sys.stdout.write('\n'.join(output) + '\n')

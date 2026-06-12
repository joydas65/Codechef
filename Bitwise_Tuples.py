import sys
input = sys.stdin.readline

MOD = 10**9 + 7

T = int(input())
output = []
for _ in range(T):
    N, M = map(int, input().split())
    ways_per_bit = (pow(2, N, MOD) - 1) % MOD
    answer = pow(ways_per_bit, M, MOD)
    output.append(str(answer))

sys.stdout.write("\n".join(output) + "\n")

import sys
input = sys.stdin.readline

MOD = 10**9 + 7

def total_calories_burned(num_km, calories_per_first_km):
    return (calories_per_first_km * pow(2, num_km - 1, MOD)) % MOD

T = int(input())
output = []
for _ in range(T):
    N, X = map(int, input().split())
    output.append(total_calories_burned(N, X))

sys.stdout.write('\n'.join(map(str, output)) + '\n')

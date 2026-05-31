import sys
input = sys.stdin.readline

def min_shopping_time(N, X, A):
    total_visits = N * X

    capacity_per_hour = sum(min(a, X) for a in A)
    bound_total = (total_visits + capacity_per_hour - 1) // capacity_per_hour  # ceil

    # Per-shop bottleneck: each shop needs ceil(X / A_i) hours
    bound_shop = max((X + a - 1) // a for a in A)

    return max(N, bound_total, bound_shop)

T = int(input())
output = []
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    output.append(str(min_shopping_time(N, X, A)))

sys.stdout.write('\n'.join(output) + '\n')

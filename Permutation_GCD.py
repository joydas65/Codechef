import sys
input = sys.stdin.readline

T = int(input())
out = []
for _ in range(T):
    N, X = map(int, input().split())
    if X < N or X > 2 * N - 1:
        out.append("-1")
        continue
    k = X - N + 1  # the first element; in [1, N]
    if k == 1:
        out.append(' '.join(map(str, range(1, N + 1))))
    else:
        rest = [i for i in range(2, N + 1) if i != k]
        out.append(' '.join(map(str, [k, 1] + rest)))
print('\n'.join(out))

import sys
input = sys.stdin.readline

T = int(input())
out = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    mx = max(A)
    limit = 2 * mx
    marked = bytearray(limit + 1)
    for a in A:
        for k in range(0, limit + 1, a):
            marked[k] = 1
    prev = 0
    best = 0
    for i in range(1, limit + 1):
        if marked[i]:
            if i - prev > best:
                best = i - prev
            prev = i
    out.append(str(best))
print('\n'.join(out))

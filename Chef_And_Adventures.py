import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    output = []
    for _ in range(t):
        n, m, x, y = int(data[idx]), int(data[idx+1]), int(data[idx+2]), int(data[idx+3])
        idx += 4
        # Without ShareChat: 1 + a*x == n and 1 + b*y == m
        no_sharechat = (n - 1) % x == 0 and (m - 1) % y == 0
        # With ShareChat (once): 2 + a*x == n and 2 + b*y == m
        with_sharechat = n >= 2 and m >= 2 and (n - 2) % x == 0 and (m - 2) % y == 0
        output.append("Chefirnemo" if no_sharechat or with_sharechat else "Pofik")
    print("\n".join(output))

solve()

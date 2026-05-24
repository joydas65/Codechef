import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    output = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        s = data[idx]; idx += 1
        # Count runs: 1 + number of adjacent pairs that differ
        m = 1 + sum(1 for i in range(1, n) if s[i] != s[i-1])
        # Optimal: place chosen plank in middle run → ceil((m-1)/2) = m//2 paints
        output.append(str(m // 2))
    print("\n".join(output))

solve()

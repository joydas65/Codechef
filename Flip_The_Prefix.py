import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        s = next(it)
        pref = [0] * n
        for i in range(1, n):
            pref[i] = pref[i - 1] + (1 if s[i] != s[i - 1] else 0)
        best = None
        for start in range(0, n - k + 1):
            last = start + k - 1
            inner = pref[last] - pref[start]
            extra = 1 if s[last] == 48 else 0
            v = inner + extra
            if best is None or v < best:
                best = v
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")

main()

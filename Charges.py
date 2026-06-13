import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        s = bytearray(next(it))
        for i in range(n):
            s[i] -= 48
        e = 0
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                e += 1
        base = n - 1
        for _ in range(k):
            p = int(next(it)) - 1
            if p > 0 and s[p - 1] == s[p]:
                e -= 1
            if p + 1 < n and s[p] == s[p + 1]:
                e -= 1
            s[p] ^= 1
            if p > 0 and s[p - 1] == s[p]:
                e += 1
            if p + 1 < n and s[p] == s[p + 1]:
                e += 1
            out.append(base + e)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()

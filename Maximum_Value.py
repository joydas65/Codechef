import sys

def main():
    data = sys.stdin.buffer
    t = int(data.readline())
    out = []
    for _ in range(t):
        n = int(data.readline())
        a = list(map(int, data.readline().split()))
        a.sort()
        idxs = sorted(set([0, 1, n - 2, n - 1]))
        best = None
        L = len(idxs)
        for i in range(L):
            for j in range(i + 1, L):
                x = a[idxs[i]]
                y = a[idxs[j]]
                v = x * y + abs(x - y)
                if best is None or v > best:
                    best = v
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")

main()

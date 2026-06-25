import sys

def main():
    data = sys.stdin.buffer
    t = int(data.readline())
    out = []
    for _ in range(t):
        n, k = map(int, data.readline().split())
        a = data.readline().split()
        b = data.readline().split()
        if any(len(x) != len(y) for x, y in zip(a, b)):
            out.append("NO")
            continue
        blob_a = b''.join(a)
        blob_b = b''.join(b)
        cost = 0
        for d in range(48, 58):
            ca = blob_a.count(bytes((d,)))
            cb = blob_b.count(bytes((d,)))
            if ca > cb:
                cost += ca - cb
        out.append("YES" if cost <= k else "NO")
    sys.stdout.write("\n".join(out) + "\n")

main()

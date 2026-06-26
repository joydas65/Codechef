import sys

def main():
    data = sys.stdin.buffer
    t = int(data.readline())
    out = []
    for _ in range(t):
        n = int(data.readline())
        a = list(map(int, data.readline().split()))
        m = max(a)
        seen = set()
        add = seen.add
        b = []
        ap = b.append
        for x in a:
            if x in seen:
                ap(m)
            else:
                add(x)
                ap(x)
        out.append(' '.join(map(str, b)))
    sys.stdout.write("\n".join(out) + "\n")

main()

import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        s = next(it)
        run = 0
        ok = True
        for ch in reversed(s):
            run += 1 if ch == 49 else -1
            if run > 1 or run < -1:
                ok = False
                break
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")

main()

import sys

def main():
    data = sys.stdin.buffer
    q = int(data.readline())
    out = []
    for _ in range(q):
        n = int(data.readline())
        s = data.readline().strip()
        t = data.readline().strip()
        a = b = c = d = 0
        for x, y in zip(s, t):
            if x == 49:
                if y == 49:
                    a += 1
                else:
                    b += 1
            else:
                if y == 49:
                    c += 1
                else:
                    d += 1
        ans = min(b, c) + min(a, (a + abs(b - c) + d) // 2)
        out.append(str(ans))
    sys.stdout.write("\n".join(out) + "\n")

main()

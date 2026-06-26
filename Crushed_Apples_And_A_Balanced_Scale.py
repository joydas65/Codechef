import sys

def main():
    data = sys.stdin.buffer
    t = int(data.readline())
    out = []
    for _ in range(t):
        m, n = map(int, data.readline().split())
        mo = m // (m & (-m))
        if n <= m and n % mo == 0:
            out.append("YES")
        else:
            out.append("NO")
    sys.stdout.write("\n".join(out) + "\n")

main()

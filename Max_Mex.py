import sys

def main():
    data = sys.stdin.buffer
    out = []
    t = int(data.readline())
    for _ in range(t):
        n, m = map(int, data.readline().split())
        a = data.readline().split()
        seen = bytearray(m)
        distinct = 0
        cnt_m = 0
        for tok in a:
            v = int(tok)
            if v == m:
                cnt_m += 1
            elif v < m:
                if not seen[v]:
                    seen[v] = 1
                    distinct += 1
        if distinct == m - 1:
            out.append(str(n - cnt_m))
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")

main()

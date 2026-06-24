import sys

def main():
    data = sys.stdin.buffer
    out = []
    t = int(data.readline())
    for _ in range(t):
        n, m = map(int, data.readline().split())
        x1, y1 = map(int, data.readline().split())
        x2, y2 = map(int, data.readline().split())
        p1 = (x1 + y1) & 1
        p2 = (x2 + y2) & 1
        if p1 != p2:
            a = ['1' if (j & 1) == 0 else '2' for j in range(m)]
            b = ['2' if (j & 1) == 0 else '1' for j in range(m)]
            sa = ' '.join(a)
            sb = ' '.join(b)
            for i in range(1, n + 1):
                if ((i + 1) & 1) == p1:
                    out.append(sa)
                else:
                    out.append(sb)
        else:
            a = ['1' if (j & 1) == 0 else '3' for j in range(m)]
            b = ['3' if (j & 1) == 0 else '1' for j in range(m)]
            sa = ' '.join(a)
            sb = ' '.join(b)
            for i in range(1, n + 1):
                if i == x2:
                    row = a[:] if ((i + 1) & 1) == p1 else b[:]
                    row[y2 - 1] = '2'
                    out.append(' '.join(row))
                elif ((i + 1) & 1) == p1:
                    out.append(sa)
                else:
                    out.append(sb)
    sys.stdout.write('\n'.join(out) + '\n')

main()

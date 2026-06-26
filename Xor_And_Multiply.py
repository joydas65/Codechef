import sys

def main():
    data = sys.stdin.buffer
    t = int(data.readline())
    out = []
    for _ in range(t):
        n, a, b = map(int, data.readline().split())
        mask = (1 << n) - 1
        c = a ^ b
        base = (~c) & mask
        if c == 0:
            p = base
        else:
            p = base | (1 << (c.bit_length() - 1))
        out.append(str(a ^ p))
    sys.stdout.write("\n".join(out) + "\n")

main()

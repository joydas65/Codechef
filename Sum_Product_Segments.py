import sys
from math import isqrt

def main():
    data = sys.stdin.buffer
    out = []
    t = int(data.readline())
    for _ in range(t):
        x, y = map(int, data.readline().split())
        sl = x // 2
        sr = x - sl
        d = isqrt(y)
        while y % d != 0:
            d -= 1
        pl = d
        pr = y // d
        if sr < pl:
            out.append(str(sl) + " " + str(sr))
            out.append(str(pl) + " " + str(pr))
        elif pr < sl:
            out.append(str(pl) + " " + str(pr))
            out.append(str(sl) + " " + str(sr))
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")

main()

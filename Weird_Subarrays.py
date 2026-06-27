import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        P = [int(next(it)) for _ in range(n)]
        is_peak = [False] * n
        for i in range(1, n - 1):
            if P[i - 1] < P[i] > P[i + 1]:
                is_peak[i] = True
        nextpeak = n
        last = n - 1
        total = 0
        for l in range(n - 1, -1, -1):
            j = l + 1
            if j <= last and is_peak[j]:
                nextpeak = j
            lim = nextpeak if nextpeak <= last else last
            total += lim - l + 1
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")

main()

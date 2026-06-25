import sys

def main():
    data = sys.stdin.buffer
    t = int(data.readline())
    out = []
    for _ in range(t):
        n = int(data.readline())
        a = list(map(int, data.readline().split()))
        if n <= 2:
            out.append(str(sum(a)))
            continue
        pre = [0] * n
        pre[0] = a[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] if pre[i - 1] > a[i] else a[i]
        suf = [0] * n
        suf[n - 1] = a[n - 1]
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] if suf[i + 1] > a[i] else a[i]
        total = a[0] + a[n - 1]
        for i in range(1, n - 1):
            ml = pre[i - 1]
            mr = suf[i + 1]
            mm = ml if ml < mr else mr
            total += a[i] if a[i] > mm else mm
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")

main()

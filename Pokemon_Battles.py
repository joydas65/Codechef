import sys

def main():
    data = sys.stdin.buffer
    t = int(data.readline())
    out = []
    for _ in range(t):
        n = int(data.readline())
        A = list(map(int, data.readline().split()))
        B = list(map(int, data.readline().split()))
        pts = sorted(zip(A, B), reverse=True)
        maxb = 0
        cnt = 0
        for a, b in pts:
            if b > maxb:
                cnt += 1
                maxb = b
        out.append(str(cnt))
    sys.stdout.write("\n".join(out) + "\n")

main()

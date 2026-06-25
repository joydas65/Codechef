import sys

def main():
    data = sys.stdin.buffer
    t = int(data.readline())
    out = []
    for _ in range(t):
        n = int(data.readline())
        w = list(map(int, data.readline().split()))
        m = max(w)
        h = n // 2
        diff = [0] * (n + 1)
        for j in range(n):
            if w[j] == m:
                s = (n - j) % n
                e = s + h
                if e <= n:
                    diff[s] += 1
                    diff[e] -= 1
                else:
                    diff[s] += 1
                    diff[n] -= 1
                    diff[0] += 1
                    diff[e - n] -= 1
        valid = 0
        cur = 0
        for k in range(n):
            cur += diff[k]
            if cur == 0:
                valid += 1
        out.append(str(valid))
    sys.stdout.write("\n".join(out) + "\n")

main()

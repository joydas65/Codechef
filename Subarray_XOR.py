import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    t = int(next(it))
    M = 998244353
    out = []
    for _ in range(t):
        n = int(next(it))
        s = next(it)
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = pow2[i - 1] * 2 % M
        run = 0
        ans = 0
        for k in range(n):
            if s[k] == 49:
                run ^= (k + 1) & 1
            if run:
                ans += pow2[n - 1 - k]
                if ans >= M:
                    ans -= M
        out.append(str(ans % M))
    sys.stdout.write("\n".join(out) + "\n")

main()

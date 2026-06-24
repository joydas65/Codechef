import sys
from itertools import accumulate

def main():
    data = sys.stdin.buffer
    t = int(data.readline())
    out = []
    for _ in range(t):
        n, k = map(int, data.readline().split())
        s = data.readline().strip()                      # bytes, length n
        # diff[t] = 1 if adjacent chars of S differ
        diff = [a != b for a, b in zip(s, s[1:])]         # bools act as 0/1
        p = list(accumulate(diff, initial=0))             # prefix sums, length n
        # total = sum over every length-K window of diff
        #       = sum(p[k:n]) - sum(p[:n-k])
        total = sum(p[k:n]) - sum(p[:n - k])
        out.append(str(total))
    sys.stdout.write('\n'.join(out) + '\n')

main()

import sys


def main():
    data = sys.stdin.buffer
    t = int(data.readline())
    out = []
    for _ in range(t):
        a, b = map(int, data.readline().split())
        s = b - a                      # p + q is always B - A
        if s == 0:                     # A == B: only X = A, sum is 0
            out.append('0')
        elif s % 2 == 0:               # even, A != B: make both halves odd
            out.append(str(s // 2 + 1))
        else:                          # odd: forced opposite parity
            out.append(str((s + 1) // 2))
    sys.stdout.write('\n'.join(out) + '\n')


main()

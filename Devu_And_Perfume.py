import sys

def main():
    rd = sys.stdin.buffer.readline
    t = int(rd())
    out = []
    for _ in range(t):
        n, m = map(int, rd().split())
        min_r = n          # sentinel larger than any valid row index
        max_r = -1
        min_c = m          # sentinel larger than any valid col index
        max_c = -1
        for r in range(n):
            row = rd()
            left = row.find(b'*')          # leftmost '*' in this row (C-level scan)
            if left != -1:
                if r < min_r:
                    min_r = r
                max_r = r
                if left < min_c:
                    min_c = left
                right = row.rfind(b'*')     # rightmost '*' in this row
                if right > max_c:
                    max_c = right
        if max_r == -1:                    # no inhabited houses
            out.append('0')
        else:
            radius = max((max_r - min_r + 1) // 2,   # ceil(diff/2)
                         (max_c - min_c + 1) // 2)
            out.append(str(1 + radius))
    sys.stdout.write('\n'.join(out) + '\n')

main()

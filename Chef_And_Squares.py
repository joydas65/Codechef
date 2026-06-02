import sys

def best_shift_and_grid(K):
    c = (K - 1) // 2  # 0-indexed center
    
    # For a given shift, 1s are where (i+j+shift) % K == 0.
    # Min distance from center to such a cell:
    def min_dist(shift):
        best = None
        # 1s lie on diagonals i+j = m where (m+shift) % K == 0
        # candidate sums m in [0, 2K-2] with (m+shift)%K==0
        for m in range((-shift) % K, 2*K - 1, K):
            # nearest cell on diagonal i+j=m to center (c,c): dist = |m - 2c| if reachable
            # cell exists with i,j in [0,K-1] and i+j=m; closest manhattan to (c,c)
            lo = max(0, m - (K - 1))
            hi = min(K - 1, m)
            # i ranges [lo,hi]; minimize |i-c| + |(m-i)-c| = |i-c| + |m-i-c|
            # this is minimized when i as close to splitting; min value = max(|m-2c|, ...)
            # Actually min over i of |i-c|+|m-i-c|; the term = distance, min = |m - 2c| if a valid i near c exists
            target_i = c  # try i=c
            best_here = None
            for i in (max(lo, min(hi, c)), lo, hi):
                j = m - i
                d = abs(i - c) + abs(j - c)
                if best_here is None or d < best_here:
                    best_here = d
            if best is None or best_here < best:
                best = best_here
        return best if best is not None else 0
    
    best_shift = max(range(K), key=min_dist)
    return best_shift

def main():
    data = sys.stdin.buffer.read().split()
    T = int(data[0])
    out = []
    for t in range(1, T + 1):
        K = int(data[t])
        shift = best_shift_and_grid(K)
        for i in range(K):
            row = ' '.join(str(((i + j + shift) % K) + 1) for j in range(K))
            out.append(row)
    sys.stdout.write('\n'.join(out) + '\n')

main()

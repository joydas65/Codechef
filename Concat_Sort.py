import sys
from bisect import bisect_left

def solve(a, n):
    sorted_vals = sorted(set(a))
    rank = {v: i for i, v in enumerate(sorted_vals)}
    m = len(sorted_vals)

    positions = [[] for _ in range(m)]
    for idx, v in enumerate(a):
        positions[rank[v]].append(idx)

    maxPosPrefix = [-1] * (m + 1)            # max index among classes 0..t-1
    for tt in range(1, m + 1):
        maxPosPrefix[tt] = max(maxPosPrefix[tt - 1], positions[tt - 1][-1])

    INF = n
    minPosSuffix = [INF] * m                  # min index among classes t+1..m-1
    for tt in range(m - 2, -1, -1):
        minPosSuffix[tt] = min(minPosSuffix[tt + 1], positions[tt + 1][0])

    i_failA = m                               # first class where "< v" stops being sorted
    for i in range(m):
        if positions[i][0] > maxPosPrefix[i]:
            continue
        i_failA = i
        break

    i_failB = -1                              # last class breaking "> v" sorted
    for i in range(m - 1, -1, -1):
        if positions[i][-1] < minPosSuffix[i]:
            continue
        i_failB = i
        break

    lo_t = max(0, i_failB)
    hi_t = min(m - 1, i_failA)
    for tcl in range(lo_t, hi_t + 1):
        lastL = maxPosPrefix[tcl]
        firstH = minPosSuffix[tcl]
        if firstH > lastL:
            return True
        pos = positions[tcl]
        j = bisect_left(pos, firstH)
        if j == len(pos) or pos[j] > lastL:
            return True
    return False

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        out.append("YES" if solve(a, n) else "NO")
    sys.stdout.write("\n".join(out) + "\n")

main()

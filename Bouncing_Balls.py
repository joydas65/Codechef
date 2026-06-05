import sys

def count_ways(N, A):
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + A[i]
    total_sum = prefix[N]

    total = 0
    i = 0
    while i < N:
        if A[i] == 0:
            j = i
            while j < N and A[j] == 0:
                j += 1
            gap = j - i
            sumL = prefix[i]                 # wall mass strictly left of the gap
            sumR = total_sum - prefix[j]      # wall mass strictly right of the gap
            # push right valid?
            if sumR == sumL or sumR == sumL + 1:
                total += gap
            # push left valid?
            if sumL == sumR or sumL == sumR + 1:
                total += gap
            i = j
        else:
            i += 1
    return total

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    out = []
    for _ in range(T):
        N = int(data[idx]); idx += 1
        A = [int(data[idx + k]) for k in range(N)]
        idx += N
        out.append(str(count_ways(N, A)))
    sys.stdout.write('\n'.join(out) + '\n')

main()

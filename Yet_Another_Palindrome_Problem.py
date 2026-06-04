import sys

def min_ops_to_palindrome(A):
    n = len(A)
    cl_prev = 0   # c value of the left index just toward center
    cr_prev = 0   # c value of the right index just toward center
    c0 = 0

    for l in range((n - 1) // 2, -1, -1):
        r = n - 1 - l
        if l == r:                       # middle element (odd n)
            c0 = cl_prev
            continue
        diff = A[r] - A[l]               # need c_l - c_r = diff
        lo = max(0, cl_prev - diff)      # c_r >= cl_prev - diff, and >= 0
        if lo > cr_prev:                 # would break non-increasing chain
            return -1
        cr = lo
        cl = cr + diff
        if cl < 0 or cr < 0:
            return -1
        cl_prev, cr_prev = cl, cr
        c0 = cl                          # leftmost = current max
    return c0

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    out = []
    for _ in range(T):
        N = int(data[idx]); idx += 1
        A = [int(data[idx + k]) for k in range(N)]
        idx += N
        out.append(str(min_ops_to_palindrome(A)))
    sys.stdout.write('\n'.join(out) + '\n')

main()

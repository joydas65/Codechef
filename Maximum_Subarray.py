import sys
from itertools import accumulate

input = sys.stdin.readline


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))

    # -----------------------------------------------------------------------
    # Key insight:
    # We must consume ALL M elements of B.  We choose a split point i (0..M):
    #   - take i elements from B's left  (B[0..i-1])
    #   - take M-i elements from B's right (B[M-i..M-1])
    # Each chosen element can be placed independently at front or back of A,
    # so we can arrange them in any order on their respective sides.
    # Therefore the best we can do with those elements is to include all
    # positive ones in our subarray (greedy).
    #
    # The maximum subarray of the final array can span:
    #   [some contiguous suffix of left_additions]
    #   + [some contiguous portion of A]
    #   + [some contiguous prefix of right_additions]
    # But since we can arrange each side's elements freely, "contiguous suffix
    # of additions" is just "any subset of positives" from that side.
    #
    # So for split i the best value is:
    #   best_left[i] + best_mid + best_right[M-i]
    # where:
    #   best_left[i]  = sum of positive elements in B[0..i-1]
    #   best_right[j] = sum of positive elements in B[j..M-1]
    #   best_mid is the best subarray that uses SOME of A, which equals one of:
    #     a) Kadane on A alone (pure A subarray)
    #     b) max_prefix_sum_of_A  (starts from A[0], used when left_additions
    #                               extend into A from the left)
    #     c) max_suffix_sum_of_A  (ends at A[N-1], used when right_additions
    #                               extend into A from the right)
    #     d) total_sum_of_A       (left + full A + right)
    #     e) 0                    (empty subarray; the additions alone are fine)
    # -----------------------------------------------------------------------

    # --- Precompute best_left[i] = sum of positives in B[0..i-1] -----------
    best_left = [0] * (M + 1)   # best_left[0] = 0 (no elements chosen)
    for i in range(1, M + 1):
        gain = B[i - 1] if B[i - 1] > 0 else 0
        best_left[i] = best_left[i - 1] + gain

    # --- Precompute best_right[j] = sum of positives in B[j..M-1] ----------
    best_right = [0] * (M + 1)  # best_right[M] = 0 (no elements chosen)
    for j in range(M - 1, -1, -1):
        gain = B[j] if B[j] > 0 else 0
        best_right[j] = best_right[j + 1] + gain

    # --- Precompute subarray statistics on A --------------------------------
    # max_prefix_sum: best sum of A[0..k] for any k (can be empty = 0)
    max_prefix_sum = 0
    running = 0
    for a in A:
        running += a
        if running > max_prefix_sum:
            max_prefix_sum = running

    # max_suffix_sum: best sum of A[k..N-1] for any k (can be empty = 0)
    max_suffix_sum = 0
    running = 0
    for a in reversed(A):
        running += a
        if running > max_suffix_sum:
            max_suffix_sum = running

    # Kadane's algorithm: best contiguous subarray of A (can be empty = 0)
    kadane_best = 0
    current = 0
    for a in A:
        current = max(0, current + a)
        if current > kadane_best:
            kadane_best = current

    total_A = sum(A)

    # -----------------------------------------------------------------------
    # Enumerate all splits i = 0..M and compute the answer for each
    # -----------------------------------------------------------------------
    answer = 0

    for i in range(M + 1):
        left_gain  = best_left[i]       # gain from B's prefix (0..i-1)
        right_gain = best_right[i]      # gain from B's suffix (i..M-1)

        # Case 1: subarray is entirely within additions (no A used)
        candidate = left_gain + right_gain

        # Case 2: subarray uses some of A (not touching additions on either side)
        candidate = max(candidate, kadane_best)

        # Case 3: left additions + prefix of A
        candidate = max(candidate, left_gain + max_prefix_sum)

        # Case 4: suffix of A + right additions
        candidate = max(candidate, max_suffix_sum + right_gain)

        # Case 5: left additions + all of A + right additions
        candidate = max(candidate, left_gain + total_A + right_gain)

        if candidate > answer:
            answer = candidate

    print(answer)


T = int(input())
for _ in range(T):
    solve()

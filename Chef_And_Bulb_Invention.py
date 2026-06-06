import sys

def days_until_invention(n, p, k):
    remainder = p % k
    full_cycles = n // k          # times each remainder appears, at minimum
    leftover = n % k              # remainders 0..leftover-1 get one extra

    # Indices tested in all groups before group `remainder`.
    indices_before = remainder * full_cycles + min(remainder, leftover)

    # Position of p within its own group (1-indexed).
    position_in_group = (p - remainder) // k + 1

    return indices_before + position_in_group

def main():
    tokens = iter(sys.stdin.buffer.read().split())
    t = int(next(tokens))
    results = []
    for _ in range(t):
        n = int(next(tokens)); p = int(next(tokens)); k = int(next(tokens))
        results.append(str(days_until_invention(n, p, k)))
    sys.stdout.write('\n'.join(results) + '\n')

main()

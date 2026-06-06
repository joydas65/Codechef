import sys

def can_make_all_equal(n, arr):
    if n % 2 == 1:
        return True
    total_xor = 0
    for value in arr:
        total_xor ^= value
    return total_xor == 0

def main():
    tokens = iter(sys.stdin.buffer.read().split())

    test_cases = int(next(tokens))
    results = []
    for _ in range(test_cases):
        n = int(next(tokens))
        arr = [int(next(tokens)) for _ in range(n)]
        results.append("YES" if can_make_all_equal(n, arr) else "NO")

    sys.stdout.write('\n'.join(results) + '\n')

main()

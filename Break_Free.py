import sys

MOD = 10**9 + 7

def count_good_removals(array):
    even_count = sum(1 for value in array if value % 2 == 0)
    odd_count = len(array) - even_count

    ways_to_choose_evens = pow(2, even_count, MOD)

    if odd_count == 0:
        # Every removal keeps an all-even array; just exclude the empty removal.
        return (ways_to_choose_evens - 1) % MOD
    else:
        # All odds are forced out, so every choice is a non-empty removal.
        return ways_to_choose_evens

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    test_cases = int(data[idx]); idx += 1

    results = []
    for _ in range(test_cases):
        n = int(data[idx]); idx += 1
        array = data[idx:idx + n]; idx += n
        array = list(map(int, array))
        results.append(str(count_good_removals(array)))

    sys.stdout.write('\n'.join(results) + '\n')

main()

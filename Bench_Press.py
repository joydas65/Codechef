import sys
from collections import Counter

def can_satisfy(num_weights, target, rod_weight, weights):
    value_counts = Counter(weights)

    max_liftable = rod_weight
    for value, count in value_counts.items():
        pairs = count // 2
        max_liftable += pairs * 2 * value

    return max_liftable >= target

def main():
    tokens = iter(sys.stdin.buffer.read().split())

    test_cases = int(next(tokens))
    results = []
    for _ in range(test_cases):
        num_weights = int(next(tokens))
        target = int(next(tokens))
        rod_weight = int(next(tokens))
        weights = [int(next(tokens)) for _ in range(num_weights)]
        results.append("YES" if can_satisfy(num_weights, target, rod_weight, weights) else "NO")

    sys.stdout.write('\n'.join(results) + '\n')

main()

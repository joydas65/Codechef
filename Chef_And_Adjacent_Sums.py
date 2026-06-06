import sys

def has_valid_rearrangement(arr):
    arr.sort()
    n = len(arr)
    largest = arr[-1]
    second_largest = arr[-2]
    smallest = arr[0]

    if largest > second_largest:
        # Only the max is constrained: it just needs one neighbor
        # strictly smaller than the second-largest value.
        return smallest < second_largest
    else:
        # Max value repeats; the only bad adjacency is max-next-to-max.
        # Those copies must be mutually non-adjacent: count <= ceil(N/2).
        max_count = arr.count(largest)   # arr is sorted; O(n) is fine here
        return max_count <= (n + 1) // 2

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    test_cases = int(data[idx]); idx += 1

    results = []
    for _ in range(test_cases):
        n = int(data[idx]); idx += 1
        arr = list(map(int, data[idx:idx + n])); idx += n
        results.append("YES" if has_valid_rearrangement(arr) else "NO")

    sys.stdout.write('\n'.join(results) + '\n')

main()

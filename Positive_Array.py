import sys

def min_positive_arrays(n, arr):
    # value_count[v] = how many elements equal v (values are in 1..n)
    value_count = [0] * (n + 1)
    for value in arr:
        value_count[value] += 1

    answer = 0
    elements_so_far = 0          # running cnt_leq[k]
    for k in range(1, n + 1):
        elements_so_far += value_count[k]
        arrays_needed = (elements_so_far + k - 1) // k   # ceil division
        if arrays_needed > answer:
            answer = arrays_needed
    return answer

def main():
    tokens = iter(sys.stdin.buffer.read().split())

    test_cases = int(next(tokens))
    results = []
    for _ in range(test_cases):
        n = int(next(tokens))
        arr = [int(next(tokens)) for _ in range(n)]
        results.append(str(min_positive_arrays(n, arr)))

    sys.stdout.write('\n'.join(results) + '\n')

main()

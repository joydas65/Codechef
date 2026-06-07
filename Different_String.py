import sys

def find_different_string(binary_strings):
    # Cantor diagonalization: flip the i-th bit of the i-th string.
    result_chars = []
    for i, string in enumerate(binary_strings):
        result_chars.append('1' if string[i] == '0' else '0')
    return ''.join(result_chars)

def main():
    tokens = iter(sys.stdin.buffer.read().split())

    test_cases = int(next(tokens))
    results = []
    for _ in range(test_cases):
        n = int(next(tokens))
        binary_strings = [next(tokens).decode() for _ in range(n)]
        results.append(find_different_string(binary_strings))

    sys.stdout.write('\n'.join(results) + '\n')

main()

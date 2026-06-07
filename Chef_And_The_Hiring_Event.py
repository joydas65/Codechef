import sys
input = sys.stdin.readline


def kth_magical_number(K):
    even_digits = [0, 2, 4, 6, 8]

    if K == 1:
        return 0

    base5_digits = []
    n = K - 1
    while n > 0:
        base5_digits.append(n % 5)
        n //= 5
    base5_digits.reverse()

    return int("".join(str(even_digits[d]) for d in base5_digits))


T = int(input())
output_lines = []
for _ in range(T):
    K = int(input())
    output_lines.append(str(kth_magical_number(K)))

sys.stdout.write("\n".join(output_lines) + "\n")

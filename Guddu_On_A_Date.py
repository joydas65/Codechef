import sys
input = sys.stdin.readline

def nth_round_integer(N):
    digit_sum = 0
    temp = N
    while temp:
        digit_sum += temp % 10
        temp //= 10
    last_digit = (10 - digit_sum % 10) % 10
    return N * 10 + last_digit

T = int(input())
output = []
for _ in range(T):
    N = int(input())
    output.append(str(nth_round_integer(N)))

sys.stdout.write('\n'.join(output) + '\n')

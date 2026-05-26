def digit_sum(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

def count_valid_X(N):
    count = 0
    for x in range(max(1, N - 99), N):
        if x + digit_sum(x) + digit_sum(digit_sum(x)) == N:
            count += 1
    return count

N = int(input())
print(count_valid_X(N))

import sys
input = sys.stdin.readline

MAX_H = 10**6

# Sieve of Eratosthenes up to MAX_H
is_prime = bytearray([1]) * (MAX_H + 1)
is_prime[0] = is_prime[1] = 0
for i in range(2, int(MAX_H**0.5) + 1):
    if is_prime[i]:
        is_prime[i*i : MAX_H+1 : i] = bytearray(len(range(i*i, MAX_H+1, i)))

def min_moves_to_kill(H):
    best = -1
    k = 0
    while (1 << k) - 1 <= H:           # 2^k - 1 <= H
        rem = H - ((1 << k) - 1)
        if rem == 0:
            candidate = k              # pure regular attacks
        elif rem >= 2 and is_prime[rem]:
            candidate = k + 1          # regular attacks + one special
        else:
            candidate = -1
        if candidate != -1:
            if best == -1 or candidate < best:
                best = candidate
        k += 1
    return best

T = int(input())
output = []
for _ in range(T):
    H = int(input())
    output.append(str(min_moves_to_kill(H)))

sys.stdout.write('\n'.join(output) + '\n')

import sys
input = sys.stdin.readline

def temperature_after(start_temp, ambient_K, minutes):
    t = start_temp
    for _ in range(minutes):
        if t > ambient_K + 1:
            t -= 1
        elif t < ambient_K - 1:
            t += 1
        else:
            t = ambient_K
    return t

def cheapest_valid_can(cans, M, K, L, R):
    best_price = -1
    for temp, price in cans:
        final_temp = temperature_after(temp, K, M)
        if L <= final_temp <= R:
            if best_price == -1 or price < best_price:
                best_price = price
    return best_price

T = int(input())
output = []
for _ in range(T):
    N, M, K, L, R = map(int, input().split())
    cans = [tuple(map(int, input().split())) for _ in range(N)]
    output.append(str(cheapest_valid_can(cans, M, K, L, R)))

sys.stdout.write('\n'.join(output) + '\n')

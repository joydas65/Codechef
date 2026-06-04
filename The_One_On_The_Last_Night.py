import sys
import heapq

def max_card_value(N, K):
    digits = [int(c) for c in N]

    # Total useful increments capped by raising every digit to 9
    budget = min(K, sum(9 - d for d in digits))

    # Max-heap by multiplicative ratio (d+1)/d; 0 gets top priority
    heap = []
    for idx, d in enumerate(digits):
        if d < 9:
            ratio = float('inf') if d == 0 else (d + 1) / d
            heapq.heappush(heap, (-ratio, idx))

    for _ in range(budget):
        if not heap:
            break
        _, idx = heapq.heappop(heap)
        digits[idx] += 1
        d = digits[idx]
        if d < 9:
            heapq.heappush(heap, (-((d + 1) / d), idx))

    product = 1
    for d in digits:
        product *= d
    return product

def main():
    data = sys.stdin.buffer.read().split()
    T = int(data[0])
    idx = 1
    out = []
    for _ in range(T):
        N = data[idx].decode()
        K = int(data[idx + 1])
        idx += 2
        out.append(str(max_card_value(N, K)))
    sys.stdout.write('\n'.join(out) + '\n')

main()

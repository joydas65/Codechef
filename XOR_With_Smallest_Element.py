import heapq
import sys
input = sys.stdin.readline

def solve():
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))

    heapq.heapify(A)

    while Y > 0:
        smallest = heapq.heappop(A)
        xored = smallest ^ X
        if not A or xored <= A[0]:
            heapq.heappush(A, xored if Y % 2 == 1 else smallest)
            break
        heapq.heappush(A, xored)
        Y -= 1

    A.sort()
    return " ".join(map(str, A))

T = int(input())
output = []
for _ in range(T):
    output.append(solve())
sys.stdout.write("\n".join(output) + "\n")

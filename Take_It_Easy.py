import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    total = sum(A)

    if total % N != 0:
        print("No")
        continue

    avg = total // N

    possible = True
    for x in A:
        if x % 2 != avg % 2:
            possible = False
            break

    print("Yes" if possible else "No")

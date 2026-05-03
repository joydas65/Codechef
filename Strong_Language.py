import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    S = input().strip()

    count = 0
    strong = False

    for ch in S:
        if ch == '*':
            count += 1
            if count >= K:
                strong = True
                break
        else:
            count = 0

    print("YES" if strong else "NO")

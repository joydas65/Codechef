import sys
input = sys.stdin.readline

def time_to_meet(side_length, speed):
    return (2 * side_length) / (3 * speed)

T = int(input())
for _ in range(T):
    s, v = map(int, input().split())
    print(f"{time_to_meet(s, v):.7f}")

import sys
input = sys.stdin.readline


def max_mod_value(A):
    largest = largest2 = 0
    for x in A:
        if x > largest:
            largest2 = largest
            largest = x
        elif x > largest2 and x < largest:
            largest2 = x
    return largest2


T = int(input())
output = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    output.append(str(max_mod_value(A)))

sys.stdout.write("\n".join(output) + "\n")

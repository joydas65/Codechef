import sys
input = sys.stdin.readline

def min_troops_to_ruin(castle_string):
    if len(castle_string) == 0:
        return 0
    if castle_string == castle_string[::-1]:
        return 1
    return 2

T = int(input())
output = []
for _ in range(T):
    H = input().strip()
    output.append(str(min_troops_to_ruin(H)))

sys.stdout.write('\n'.join(output) + '\n')

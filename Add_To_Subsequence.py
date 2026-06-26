import sys
from collections import Counter

def main():
    data = sys.stdin.buffer
    t = int(data.readline())
    out = []
    for _ in range(t):
        n = int(data.readline())
        a = data.readline().split()
        f = max(Counter(a).values())
        out.append(str((f - 1).bit_length()))
    sys.stdout.write("\n".join(out) + "\n")

main()

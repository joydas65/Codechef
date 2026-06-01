import sys

def min_P(s):
    n = len(s)
    val = [1] * (n + 1)

    # Left to right: handle '<' (must increase) and '=' (carry forward)
    for i in range(n):
        if s[i] == '<':
            if val[i + 1] < val[i] + 1:
                val[i + 1] = val[i] + 1
        elif s[i] == '=':
            if val[i + 1] < val[i]:
                val[i + 1] = val[i]

    # Right to left: handle '>' (left must exceed right) and '=' (carry back)
    for i in range(n - 1, -1, -1):
        if s[i] == '>':
            if val[i] < val[i + 1] + 1:
                val[i] = val[i + 1] + 1
        elif s[i] == '=':
            if val[i] < val[i + 1]:
                val[i] = val[i + 1]

    return max(val)

def main():
    data = sys.stdin.buffer.read().split()
    T = int(data[0])
    out = []
    for i in range(1, T + 1):
        out.append(str(min_P(data[i].decode())))
    sys.stdout.write('\n'.join(out) + '\n')

main()

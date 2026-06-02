import sys

def longest_repeating_boring(s):
    # Collect run lengths per character
    best = 0
    i, n = 0, len(s)
    # Track top-2 run lengths per character
    top1 = [0] * 26
    top2 = [0] * 26
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        run_len = j - i
        c = ord(s[i]) - 97
        if run_len > top1[c]:
            top2[c] = top1[c]
            top1[c] = run_len
        elif run_len > top2[c]:
            top2[c] = run_len
        i = j

    for c in range(26):
        # single long run gives top1-1; two runs give top2 (=min of the two)
        candidate = max(top1[c] - 1, top2[c])
        if candidate > best:
            best = candidate
    return best

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    out = []
    for _ in range(T):
        N = int(data[idx]); idx += 1
        s = data[idx].decode(); idx += 1
        out.append(str(longest_repeating_boring(s)))
    sys.stdout.write('\n'.join(out) + '\n')

main()

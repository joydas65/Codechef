import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1

    Ns = []
    maxN = 1
    for _ in range(t):
        n = int(data[idx]); idx += 1
        Ns.append(n)
        if n > maxN:
            maxN = n

    # Smallest-prime-factor sieve, then Omega (prime factors with multiplicity)
    spf = list(range(maxN + 1))
    i = 2
    while i * i <= maxN:
        if spf[i] == i:
            for j in range(i * i, maxN + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1

    Omega = [0] * (maxN + 1)
    for i in range(2, maxN + 1):
        Omega[i] = Omega[i // spf[i]] + 1

    out = []
    for n in Ns:
        c = n.bit_length()            # floor(log2(n)) + 1
        out.append(str(c))
        out.append(' '.join(str(Omega[i] + 1) for i in range(1, n + 1)))

    sys.stdout.write('\n'.join(out) + '\n')

main()

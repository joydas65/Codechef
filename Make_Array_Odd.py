import sys
def main():
    data = sys.stdin.buffer.read().split()
    idx = 0

    numTestCases = int(data[idx]); idx += 1
    outputLines = []

    for _ in range(numTestCases):
        arraySize  = int(data[idx]); idx += 1
        xorOrValue = int(data[idx]); idx += 1
        elements   = data[idx:idx + arraySize]; idx += arraySize

        # Check parity by last ASCII digit (avoids full int conversion — faster)
        evenCount = sum(1 for element in elements if element[-1] % 2 == 0)
        oddCount  = arraySize - evenCount

        if xorOrValue & 1:
            # X is odd: result always has bit 0 = 1, so any 2-element op fixes both.
            # Pair evens together first; if 1 left over, pair with an odd. → ceil(even/2)
            outputLines.append(str((evenCount + 1) // 2))
        else:
            # X is even: only pairing one even with one odd produces an odd result.
            if evenCount == 0:
                outputLines.append('0')
            elif oddCount == 0:
                outputLines.append('-1')   # no odd elements to pair with
            else:
                outputLines.append(str(evenCount))  # one op per even (reuse any odd)

    sys.stdout.write('\n'.join(outputLines) + '\n')
main()

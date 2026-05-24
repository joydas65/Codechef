import sys

def countWellPaintedFlags(numColors):
    # 5 patterns, each with a chromatic polynomial based on adjacency graph:
    # Pattern 1 (3 vert stripes,  path P3):     N*(N-1)^2
    # Pattern 2 (3 horiz stripes, path P3):     N*(N-1)^2
    # Pattern 3 (3 pairwise-adjacent, K3):      N*(N-1)*(N-2)
    # Pattern 4 (4-region diamond, K4-1-edge):  N*(N-1)*(N-2)^2
    # Pattern 5 (4-region diamond, K4-1-edge):  N*(N-1)*(N-2)^2
    # Sum = N*(N-1) * [2*(N-1) + (N-2) + 2*(N-2)^2]
    #     = N*(N-1) * (2N^2 - 5N + 4)
    N = numColors
    return N * (N - 1) * (2 * N * N - 5 * N + 4)

def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    outputLines = []

    for _ in range(numTestCases):
        numColors = int(inputTokens[tokenIndex]); tokenIndex += 1
        outputLines.append(str(countWellPaintedFlags(numColors)))

    sys.stdout.write('\n'.join(outputLines) + '\n')

main()

import sys

def computeMaxAngriness(numPieces, maxSwaps):
    effectiveSwaps = min(maxSwaps, numPieces // 2)
    return effectiveSwaps * (2 * numPieces - 2 * effectiveSwaps - 1)

def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    answers = []

    for _ in range(numTestCases):
        numPieces = int(inputTokens[tokenIndex]); tokenIndex += 1
        maxSwaps  = int(inputTokens[tokenIndex]); tokenIndex += 1
        answers.append(str(computeMaxAngriness(numPieces, maxSwaps)))

    sys.stdout.write('\n'.join(answers) + '\n')

main()

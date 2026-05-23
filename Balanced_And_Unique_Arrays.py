import sys

def buildInterestingPair(arraySize):
    if arraySize % 4 != 0:
        return ["NO"]
    k = arraySize // 4
    arrayA = list(range(1, k + 1)) + list(range(3 * k + 1, arraySize + 1))
    arrayB = list(range(k + 1, 3 * k + 1))
    return ["YES", ' '.join(map(str, arrayA)), ' '.join(map(str, arrayB))]

def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    outputLines = []

    for _ in range(numTestCases):
        arraySize = int(inputTokens[tokenIndex]); tokenIndex += 1
        outputLines.extend(buildInterestingPair(arraySize))

    sys.stdout.write('\n'.join(outputLines) + '\n')

main()

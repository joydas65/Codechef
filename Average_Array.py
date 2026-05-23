import sys

def constructArrayWithTargetMean(arraySize, targetMean):
    halfSize = arraySize // 2
    result = []
    for value in range(targetMean - halfSize, targetMean + halfSize + 1):
        if arraySize % 2 == 0 and value == targetMean:
            continue
        result.append(value)
    return result

def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    outputLines = []

    for _ in range(numTestCases):
        arraySize  = int(inputTokens[tokenIndex]); tokenIndex += 1
        targetMean = int(inputTokens[tokenIndex]); tokenIndex += 1

        array = constructArrayWithTargetMean(arraySize, targetMean)
        outputLines.append(' '.join(map(str, array)))

    sys.stdout.write('\n'.join(outputLines) + '\n')

main()

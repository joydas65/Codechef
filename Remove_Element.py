import sys


def canReduceToOneElement(arraySize, maxAllowedPairSum, array):
    if arraySize == 1:
        return True
    return min(array) + max(array) <= maxAllowedPairSum


def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    answers = []

    for _ in range(numTestCases):
        arraySize        = int(inputTokens[tokenIndex]);     tokenIndex += 1
        maxAllowedPairSum = int(inputTokens[tokenIndex]);    tokenIndex += 1
        array = list(map(int, inputTokens[tokenIndex:tokenIndex + arraySize]))
        tokenIndex += arraySize

        answers.append("YES" if canReduceToOneElement(arraySize, maxAllowedPairSum, array) else "NO")

    sys.stdout.write("\n".join(answers) + "\n")


main()

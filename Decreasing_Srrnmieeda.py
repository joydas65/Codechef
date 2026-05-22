import sys

def findSmallestDecreasingModuloN(leftBound, rightBound):
    if rightBound < 2 * leftBound:
        return rightBound
    return -1

def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    answers = []

    for _ in range(numTestCases):
        leftBound  = int(inputTokens[tokenIndex]); tokenIndex += 1
        rightBound = int(inputTokens[tokenIndex]); tokenIndex += 1
        answers.append(str(findSmallestDecreasingModuloN(leftBound, rightBound)))

    sys.stdout.write('\n'.join(answers) + '\n')

main()

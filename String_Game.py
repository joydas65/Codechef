import sys

def determineWinner(binaryString):
    countZeros = binaryString.count('0')
    countOnes  = len(binaryString) - countZeros
    totalMoves = min(countZeros, countOnes)
    return "Zlatan" if totalMoves % 2 == 1 else "Ramos"


def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    answers = []

    for _ in range(numTestCases):
        stringLength = int(inputTokens[tokenIndex]); tokenIndex += 1
        binaryString = inputTokens[tokenIndex].decode(); tokenIndex += 1
        answers.append(determineWinner(binaryString))

    sys.stdout.write("\n".join(answers) + "\n")

main()

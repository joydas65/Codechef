import sys


def solveEquationSystem(numEquations, constants):
    totalSumOfConstants = sum(constants)
    variableTotal = totalSumOfConstants // (numEquations - 1)
    return [variableTotal - constant for constant in constants]


def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    outputLines = []

    for _ in range(numTestCases):
        numEquations = int(inputTokens[tokenIndex]); tokenIndex += 1
        constants = list(map(int, inputTokens[tokenIndex:tokenIndex + numEquations]))
        tokenIndex += numEquations

        solution = solveEquationSystem(numEquations, constants)
        outputLines.append(' '.join(map(str, solution)))

    sys.stdout.write('\n'.join(outputLines) + '\n')


main()

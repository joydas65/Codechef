import sys
from math import gcd
from functools import reduce

def computeMinAdditionalPizzaCuts(numCuts, sortedAngles):
    # Gaps between consecutive cuts (including wrap-around)
    gapList = [sortedAngles[i+1] - sortedAngles[i] for i in range(numCuts - 1)]
    gapList.append(360 + sortedAngles[0] - sortedAngles[-1])  # wrap-around gap

    # Largest valid slice size = gcd of all gaps (automatically divides 360 since gaps sum to 360)
    sliceAngleGcd = reduce(gcd, gapList)

    # Total slices with this slice size, minus existing n cuts
    return 360 // sliceAngleGcd - numCuts

def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    outputLines = []

    for _ in range(numTestCases):
        numCuts = int(inputTokens[tokenIndex]); tokenIndex += 1
        sortedAngles = list(map(int, inputTokens[tokenIndex:tokenIndex + numCuts]))
        tokenIndex += numCuts
        outputLines.append(str(computeMinAdditionalPizzaCuts(numCuts, sortedAngles)))

    sys.stdout.write('\n'.join(outputLines) + '\n')

main()

import sys

def computeMinimumSmoke(numPeople, busSmokeUnits, carSmokeUnits):
    minimumSmoke = float('inf')
    maxBusesNeeded = (numPeople + 99) // 100  # ceil(N / 100)

    for numBuses in range(maxBusesNeeded + 1):
        remainingPeople = max(0, numPeople - 100 * numBuses)
        numCars         = (remainingPeople + 3) // 4  # ceil(remaining / 4)
        totalSmoke      = numBuses * busSmokeUnits + numCars * carSmokeUnits
        if totalSmoke < minimumSmoke:
            minimumSmoke = totalSmoke

    return minimumSmoke

def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    outputLines = []

    for _ in range(numTestCases):
        numPeople      = int(inputTokens[tokenIndex]); tokenIndex += 1
        busSmokeUnits  = int(inputTokens[tokenIndex]); tokenIndex += 1
        carSmokeUnits  = int(inputTokens[tokenIndex]); tokenIndex += 1
        outputLines.append(str(computeMinimumSmoke(numPeople, busSmokeUnits, carSmokeUnits)))

    sys.stdout.write('\n'.join(outputLines) + '\n')

main()

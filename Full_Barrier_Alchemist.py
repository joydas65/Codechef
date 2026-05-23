import sys

def countBarriersCrossed(edwardHeight, duckAmount, jumpHeight, lifeForce, barriers):
    barriersPassedCount = 0
    remainingLifeForce = lifeForce

    for barrierType, barrierThreshold in barriers:
        if barrierType == 1:
            canPassNaturally = (edwardHeight - duckAmount <= barrierThreshold)
        else:
            canPassNaturally = (jumpHeight >= barrierThreshold)

        if canPassNaturally:
            barriersPassedCount += 1
        else:
            remainingLifeForce -= 1
            if remainingLifeForce == 0:
                break  # exhausted after breaking: cannot pass this barrier
            barriersPassedCount += 1

    return barriersPassedCount

def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    answers = []

    for _ in range(numTestCases):
        numBarriers  = int(inputTokens[tokenIndex]); tokenIndex += 1
        edwardHeight = int(inputTokens[tokenIndex]); tokenIndex += 1
        duckAmount   = int(inputTokens[tokenIndex]); tokenIndex += 1
        jumpHeight   = int(inputTokens[tokenIndex]); tokenIndex += 1
        lifeForce    = int(inputTokens[tokenIndex]); tokenIndex += 1

        barriers = []
        for _ in range(numBarriers):
            barrierType      = int(inputTokens[tokenIndex]); tokenIndex += 1
            barrierThreshold = int(inputTokens[tokenIndex]); tokenIndex += 1
            barriers.append((barrierType, barrierThreshold))

        answers.append(str(countBarriersCrossed(edwardHeight, duckAmount, jumpHeight, lifeForce, barriers)))

    sys.stdout.write('\n'.join(answers) + '\n')

main()

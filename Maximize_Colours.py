import sys


def computeMaxColours(redDrops, greenDrops, blueDrops):
    primaryColourCount = (redDrops > 0) + (greenDrops > 0) + (blueDrops > 0)

    maxSecondaryColours = 0

    # Single secondaries (need both components >= 2 to keep both primaries)
    if redDrops >= 2 and greenDrops >= 2:               maxSecondaryColours = max(maxSecondaryColours, 1)  # yellow
    if greenDrops >= 2 and blueDrops >= 2:              maxSecondaryColours = max(maxSecondaryColours, 1)  # cyan
    if redDrops >= 2 and blueDrops >= 2:                maxSecondaryColours = max(maxSecondaryColours, 1)  # magenta

    # Two secondaries (shared primary needs >= 3 since it's used twice)
    if redDrops >= 2 and greenDrops >= 3 and blueDrops >= 2:   maxSecondaryColours = max(maxSecondaryColours, 2)  # yellow + cyan
    if redDrops >= 3 and greenDrops >= 2 and blueDrops >= 2:   maxSecondaryColours = max(maxSecondaryColours, 2)  # yellow + magenta
    if redDrops >= 2 and greenDrops >= 2 and blueDrops >= 3:   maxSecondaryColours = max(maxSecondaryColours, 2)  # cyan + magenta

    # All three secondaries (every primary used twice, so each needs >= 3)
    if redDrops >= 3 and greenDrops >= 3 and blueDrops >= 3:   maxSecondaryColours = 3

    return primaryColourCount + maxSecondaryColours


def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    answers = []

    for _ in range(numTestCases):
        redDrops   = int(inputTokens[tokenIndex]); tokenIndex += 1
        greenDrops = int(inputTokens[tokenIndex]); tokenIndex += 1
        blueDrops  = int(inputTokens[tokenIndex]); tokenIndex += 1

        answers.append(str(computeMaxColours(redDrops, greenDrops, blueDrops)))

    sys.stdout.write("\n".join(answers) + "\n")


main()

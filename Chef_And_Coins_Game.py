import sys

def determineCoinsGameWinner(coinCount):
    # P-positions (Misha wins) = multiples of 6
    # Reason: no prime power or 1 is divisible by 6,
    # so from 6k you always land on a non-multiple,
    # and from any non-multiple you can always reach a multiple.
    return "Chef" if coinCount % 6 != 0 else "Misha"

def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    answers = []

    for _ in range(numTestCases):
        coinCount = int(inputTokens[tokenIndex]); tokenIndex += 1
        answers.append(determineCoinsGameWinner(coinCount))

    sys.stdout.write('\n'.join(answers) + '\n')

main()

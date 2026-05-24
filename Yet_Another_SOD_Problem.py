import sys

def countDigitSumDivisibleByThree(leftBound, rightBound):
    # A number n ≡ its digit sum (mod 3), so SOD divisible by 3 ↔ n divisible by 3.
    # Count multiples of 3 in [leftBound, rightBound]:
    return rightBound // 3 - (leftBound - 1) // 3

def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    outputLines = []

    for _ in range(numTestCases):
        leftBound  = int(inputTokens[tokenIndex]); tokenIndex += 1
        rightBound = int(inputTokens[tokenIndex]); tokenIndex += 1
        outputLines.append(str(countDigitSumDivisibleByThree(leftBound, rightBound)))

    sys.stdout.write('\n'.join(outputLines) + '\n')

main()

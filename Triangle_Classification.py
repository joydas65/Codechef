import sys

def classifyTriangle(subtaskId, x1, y1, x2, y2, x3, y3):
    # Squared side lengths — integer arithmetic avoids all floating-point issues
    squaredSide_a = (x2 - x3) ** 2 + (y2 - y3) ** 2
    squaredSide_b = (x1 - x3) ** 2 + (y1 - y3) ** 2
    squaredSide_c = (x1 - x2) ** 2 + (y1 - y2) ** 2

    # Side classification (equilateral triangles excluded per problem statement)
    if squaredSide_a == squaredSide_b or squaredSide_b == squaredSide_c or squaredSide_a == squaredSide_c:
        sideClass = "Isosceles"
    else:
        sideClass = "Scalene"

    if subtaskId == 1:
        return sideClass + " triangle"

    # Angle classification: sort sides, check largest vs sum of other two
    smallest, middle, largest = sorted([squaredSide_a, squaredSide_b, squaredSide_c])
    sumOfSmaller = smallest + middle

    if largest == sumOfSmaller:
        angleClass = "right"
    elif largest > sumOfSmaller:
        angleClass = "obtuse"
    else:
        angleClass = "acute"

    return sideClass + " " + angleClass + " triangle"

def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    subtaskId    = int(inputTokens[tokenIndex]); tokenIndex += 1
    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    outputLines  = []

    for _ in range(numTestCases):
        x1 = int(inputTokens[tokenIndex]); tokenIndex += 1
        y1 = int(inputTokens[tokenIndex]); tokenIndex += 1
        x2 = int(inputTokens[tokenIndex]); tokenIndex += 1
        y2 = int(inputTokens[tokenIndex]); tokenIndex += 1
        x3 = int(inputTokens[tokenIndex]); tokenIndex += 1
        y3 = int(inputTokens[tokenIndex]); tokenIndex += 1
        outputLines.append(classifyTriangle(subtaskId, x1, y1, x2, y2, x3, y3))

    sys.stdout.write('\n'.join(outputLines) + '\n')

main()

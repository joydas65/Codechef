import sys

def flipTurnDirection(direction):
    return "Right" if direction == "Left" else "Left"

def buildReversedDirections(instructions):
    roadNames = []
    turnDirections = []

    for instruction in instructions:
        parts = instruction.split()
        roadName = ' '.join(parts[2:])   # road name (may contain spaces)
        directive = parts[0]             # "Begin", "Left", or "Right"
        roadNames.append(roadName)
        if directive != "Begin":
            turnDirections.append(directive)

    reversedInstructions = [f"Begin on {roadNames[-1]}"]
    for turnIndex in range(len(turnDirections) - 1, -1, -1):
        flippedTurn = flipTurnDirection(turnDirections[turnIndex])
        reversedInstructions.append(f"{flippedTurn} on {roadNames[turnIndex]}")

    return reversedInstructions

def main():
    allLines = sys.stdin.read().splitlines()
    lineIndex = 0

    numTestCases = int(allLines[lineIndex]); lineIndex += 1
    outputBlocks = []

    for _ in range(numTestCases):
        numInstructions = int(allLines[lineIndex]); lineIndex += 1
        instructions = []
        for _ in range(numInstructions):
            instructions.append(allLines[lineIndex]); lineIndex += 1

        reversedLines = buildReversedDirections(instructions)
        outputBlocks.append('\n'.join(reversedLines))

    sys.stdout.write('\n\n'.join(outputBlocks) + '\n\n')

main()

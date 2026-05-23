import sys

def findMinimumExecutionTime(taskTimes):
    totalTime = sum(taskTimes)
    prefixTime = 0
    minimumTime = totalTime  # split at k=0: first processor idle, second takes all

    for singleTaskTime in taskTimes:
        prefixTime += singleTaskTime
        suffixTime = totalTime - prefixTime
        minimumTime = min(minimumTime, max(prefixTime, suffixTime))

    return minimumTime

def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    answers = []

    for _ in range(numTestCases):
        numTasks = int(inputTokens[tokenIndex]); tokenIndex += 1
        taskTimes = list(map(int, inputTokens[tokenIndex:tokenIndex + numTasks]))
        tokenIndex += numTasks

        answers.append(str(findMinimumExecutionTime(taskTimes)))

    sys.stdout.write('\n'.join(answers) + '\n')

main()

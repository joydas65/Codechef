import sys

def findMinimumMealTime(numDishes, requiredCategories, dishCategories, cookingTimes):
    minTimePerCategory = {}
    for category, cookTime in zip(dishCategories, cookingTimes):
        if category not in minTimePerCategory or cookTime < minTimePerCategory[category]:
            minTimePerCategory[category] = cookTime

    if len(minTimePerCategory) < requiredCategories:
        return -1

    sortedCategoryMinTimes = sorted(minTimePerCategory.values())
    return sum(sortedCategoryMinTimes[:requiredCategories])

def main():
    inputTokens = sys.stdin.buffer.read().split()
    tokenIndex = 0

    numTestCases = int(inputTokens[tokenIndex]); tokenIndex += 1
    answers = []

    for _ in range(numTestCases):
        numDishes           = int(inputTokens[tokenIndex]);     tokenIndex += 1
        requiredCategories  = int(inputTokens[tokenIndex]);     tokenIndex += 1
        dishCategories = list(map(int, inputTokens[tokenIndex:tokenIndex + numDishes]))
        tokenIndex += numDishes
        cookingTimes = list(map(int, inputTokens[tokenIndex:tokenIndex + numDishes]))
        tokenIndex += numDishes

        answers.append(str(findMinimumMealTime(numDishes, requiredCategories, dishCategories, cookingTimes)))

    sys.stdout.write('\n'.join(answers) + '\n')

main()

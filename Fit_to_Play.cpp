#include <bits/stdc++.h>
using namespace std;

int main() {
    int numTestCases;
    scanf("%d", &numTestCases);

    while (numTestCases--) {
        int numMatches;
        scanf("%d", &numMatches);

        int firstGoals;
        scanf("%d", &firstGoals);
        int minGoalsSoFar  = firstGoals;
        int bestImprovement = -1;

        for (int matchIndex = 1; matchIndex < numMatches; matchIndex++) {
            int currentGoals;
            scanf("%d", &currentGoals);

            if (currentGoals > minGoalsSoFar) {
                int improvement = currentGoals - minGoalsSoFar;
                if (improvement > bestImprovement)
                    bestImprovement = improvement;
            }
            if (currentGoals < minGoalsSoFar)
                minGoalsSoFar = currentGoals;
        }

        if (bestImprovement > 0)
            printf("%d\n", bestImprovement);
        else
            printf("UNFIT\n");
    }

    return 0;
}

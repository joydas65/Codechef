import sys
input = sys.stdin.readline


def minimum_buy_days(chocolates_per_box, daily_requirement, survival_days):
    if chocolates_per_box < daily_requirement:
        return -1

    stock = 0
    days_bought = 0
    buy_days_used = set()

    for day in range(1, survival_days + 1):
        if stock < daily_requirement:
            buy_day = day
            while buy_day >= 1 and (buy_day % 7 == 0 or buy_day in buy_days_used):
                buy_day -= 1
            if buy_day < 1:
                return -1
            buy_days_used.add(buy_day)
            stock += chocolates_per_box
            days_bought += 1
        stock -= daily_requirement

    return days_bought


T = int(input())
for _ in range(T):
    N, K, S = map(int, input().split())
    print(minimum_buy_days(N, K, S))

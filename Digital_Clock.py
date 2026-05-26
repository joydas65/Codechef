import sys
input = sys.stdin.readline

def all_digits_identical(hour, minute):
    combined_digits = str(hour) + str(minute)
    return len(set(combined_digits)) == 1

def count_identical_digit_times(total_hours, total_minutes):
    count = 0
    for hour in range(total_hours):
        for minute in range(total_minutes):
            if all_digits_identical(hour, minute):
                count += 1
    return count

T = int(input())
for _ in range(T):
    H, M = map(int, input().split())
    print(count_identical_digit_times(H, M))

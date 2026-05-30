import sys
input = sys.stdin.readline

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    days = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]
    return days[month - 1]

def pills_taken_correctly(year, month, day):
    required_parity = day % 2
    count = 0
    while True:
        # Is the current day valid (correct parity)?
        if day % 2 != required_parity:
            break
        count += 1
        # Advance two days
        day += 2
        # Roll over months/years as needed
        mlen = days_in_month(year, month)
        if day > mlen:
            day -= mlen
            month += 1
            if month > 12:
                month = 1
                year += 1
    return count

T = int(input())
output = []
for _ in range(T):
    yyyy, mm, dd = map(int, input().split(':'))
    output.append(str(pills_taken_correctly(yyyy, mm, dd)))

sys.stdout.write('\n'.join(output) + '\n')

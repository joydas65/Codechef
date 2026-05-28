import sys
import math
input = sys.stdin.readline

def station_position(i):
    return i * (i + 1) // 2

def time_via_station(station_index, cinema_x):
    # 1 min walk to station 1 + (i-1) train hops + walk from station i to X
    # = i + |pos_i - X|
    return station_index + abs(station_position(station_index) - cinema_x)

def min_travel_time(cinema_x):
    # Pure walking
    best_time = cinema_x

    # Find station index nearest to X using triangular number formula
    # i*(i+1)/2 = X  =>  i ≈ (-1 + sqrt(1 + 8X)) / 2
    approx_station = int((-1 + math.isqrt(1 + 8 * cinema_x)) // 2)

    # Check a window of nearby stations
    for station in range(max(1, approx_station - 2), approx_station + 4):
        best_time = min(best_time, time_via_station(station, cinema_x))

    return best_time

T = int(input())
output = []
for _ in range(T):
    X = int(input())
    output.append(str(min_travel_time(X)))

sys.stdout.write('\n'.join(output) + '\n')

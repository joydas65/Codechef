import sys

def main():
    data = sys.stdin.buffer.read().split()
    T = int(data[0])
    out = []
    for i in range(1, T + 1):
        s = data[i]   # bytes object
        days = 0
        cur_max = 0
        run = 0
        for c in s:                # iterating bytes yields ints
            if c == 46:            # ord('.') == 46
                run += 1
            else:                  # '#'
                if run > cur_max:
                    days += 1
                    cur_max = run
                run = 0
        out.append(str(days))
    sys.stdout.write('\n'.join(out))

main()

import sys

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(T):
        R = int(input_data[idx])
        C = int(input_data[idx+1])
        idx += 2
        
        grid = [input_data[idx+i] for i in range(R)]
        idx += R
        
        # DP tables to store the inclusive counts of contiguous '^'
        left = [[0] * C for _ in range(R)]
        right = [[0] * C for _ in range(R)]
        top = [[0] * C for _ in range(R)]
        bottom = [[0] * C for _ in range(R)]
        
        # Top-down & Left-right pass
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '^':
                    left[i][j] = left[i][j-1] + 1 if j > 0 else 1
                    top[i][j] = top[i-1][j] + 1 if i > 0 else 1
                    
        # Bottom-up & Right-left pass
        for i in range(R-1, -1, -1):
            for j in range(C-1, -1, -1):
                if grid[i][j] == '^':
                    right[i][j] = right[i][j+1] + 1 if j < C-1 else 1
                    bottom[i][j] = bottom[i+1][j] + 1 if i < R-1 else 1
                    
        monsters = 0
        
        # Evaluate each cell
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '^':
                    # Subtract 1 to exclude the current cell itself from the count
                    L = left[i][j] - 1
                    R_cnt = right[i][j] - 1
                    T_cnt = top[i][j] - 1
                    B_cnt = bottom[i][j] - 1
                    
                    # Condition: prime P <= min(L, R, T, B) is equivalent to min >= 2
                    if L >= 2 and R_cnt >= 2 and T_cnt >= 2 and B_cnt >= 2:
                        monsters += 1
                        
        out.append(str(monsters))
        
    # Print all outputs joined by a newline
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()

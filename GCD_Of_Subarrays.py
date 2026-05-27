import sys

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    out = []
    idx = 1
    
    for _ in range(T):
        N = int(input_data[idx])
        K = int(input_data[idx+1])
        idx += 2
        
        # Calculate the minimum possible sum of GCDs
        min_sum = N * (N + 1) // 2
        
        if K < min_sum:
            out.append("-1")
        else:
            # Calculate the required value for the last element
            X = K - min_sum + 1
            
            # The array consists of (N-1) ones followed by X
            ans = ["1"] * (N - 1) + [str(X)]
            out.append(" ".join(ans))
            
    # Print all results separated by a newline
    print("\n".join(out))

if __name__ == '__main__':
    solve()

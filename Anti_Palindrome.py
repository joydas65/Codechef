import sys
from collections import Counter

def solve():
    # Read all inputs from standard input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(T):
        N = int(input_data[idx])
        S = input_data[idx+1]
        idx += 2
        
        # Count character frequencies
        freq = Counter(S)
        
        # Count how many characters have an odd frequency
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        
        if N % 2 == 0:
            if odd_count > 0:
                out.append("0")
            else:
                out.append("1")
        else:
            if odd_count > 1:
                out.append("0")
            else:
                # If odd_count == 1, check if the string is made of a single unique character
                if len(freq) == 1:
                    out.append("2")
                else:
                    out.append("1")
                    
    # Print all results separated by a newline
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()

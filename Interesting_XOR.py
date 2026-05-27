import sys

def solve():
    # Read all inputs from standard input at once for fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    out = []
    
    for i in range(1, T + 1):
        C = int(input_data[i])
        
        # d is the number of bits in C
        d = C.bit_length()
        
        # Calculate 2^(d-1), which is the highest bit of C
        highest_bit = 1 << (d - 1)
        
        # A gets the highest bit. 
        # For the rest of the bits, A gets the flipped bits of C.
        mask = highest_bit - 1
        A = highest_bit | ((~C) & mask)
        
        # B is simply A XOR C
        B = A ^ C
        
        out.append(str(A * B))
        
    # Print all results joined by a newline
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()

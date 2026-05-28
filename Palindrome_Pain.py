import sys

def solve():
    # Read all inputs at once for fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    out = []
    idx = 1
    
    for _ in range(T):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        
        # Check impossible conditions
        if (x % 2 != 0 and y % 2 != 0) or x == 1 or y == 1:
            out.append("-1")
        else:
            hx = x // 2
            hy = y // 2
            
            # Determine the middle character if one count is odd
            mid = ""
            if x % 2 != 0:
                mid = "a"
            elif y % 2 != 0:
                mid = "b"
                
            # Construct the first palindrome (a's outside, b's inside)
            left1 = "a" * hx + "b" * hy
            ans1 = left1 + mid + left1[::-1]
            
            # Construct the second palindrome (b's outside, a's inside)
            left2 = "b" * hy + "a" * hx
            ans2 = left2 + mid + left2[::-1]
            
            out.append(ans1)
            out.append(ans2)
            
    # Print all results separated by newlines
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()

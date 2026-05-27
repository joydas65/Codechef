import sys
input = sys.stdin.readline

def min_ops_to_make_palindrome_possible(frequencies):
    odd_count = sum(1 for freq in frequencies if freq % 2 == 1)
    # Each operation merges two odd-freq chars → reduces odd_count by 2
    # Need odd_count <= 1, so need odd_count // 2 operations
    return odd_count // 2

T = int(input())
output = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    output.append(str(min_ops_to_make_palindrome_possible(A)))

sys.stdout.write('\n'.join(output) + '\n')

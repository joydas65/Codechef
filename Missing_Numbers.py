import sys

def find_ab(nums):
    from collections import Counter
    target = Counter(nums)
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            s = nums[i]   # candidate a+b
            d = nums[j]   # candidate a-b
            # a = (s+d)/2, b = (s-d)/2
            if (s + d) % 2 != 0:
                continue
            a = (s + d) // 2
            b = (s - d) // 2
            if not (1 <= a <= 10**4 and 1 <= b <= 10**4):
                continue
            produced = Counter([a + b, a - b, a * b, a // b])
            if produced == target:
                return a, b
    return -1, -1

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    out = []
    for _ in range(T):
        nums = [int(data[idx + k]) for k in range(4)]
        idx += 4
        a, b = find_ab(nums)
        out.append(f"{a} {b}")
    sys.stdout.write('\n'.join(out) + '\n')

main()

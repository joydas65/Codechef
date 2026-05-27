import sys
input = sys.stdin.readline

LANG1 = set('abcdefghijklm')          # lowercase a-m
LANG2 = set('NOPQRSTUVWXYZ')          # uppercase N-Z

def is_valid_word(word):
    # All chars must belong to exactly one language
    chars = set(word)
    if chars <= LANG1:
        return True
    if chars <= LANG2:
        return True
    return False   # mixed languages OR invalid character

def is_valid_sentence(words):
    return all(is_valid_word(word) for word in words)

T = int(input())
output = []
for _ in range(T):
    line = input().split()
    K = int(line[0])
    words = line[1 : K + 1]
    output.append("YES" if is_valid_sentence(words) else "NO")

sys.stdout.write('\n'.join(output) + '\n')

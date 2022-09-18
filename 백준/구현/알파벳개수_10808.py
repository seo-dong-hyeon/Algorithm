import sys
from string import ascii_lowercase

S = sys.stdin.readline().rstrip()
alphabets = list(ascii_lowercase)

for alphabet in alphabets:
    print(S.count(alphabet), end=' ')
print()

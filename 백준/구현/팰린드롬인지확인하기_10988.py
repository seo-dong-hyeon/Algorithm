import sys

S = sys.stdin.readline().rstrip()
print(int(S == S[::-1]))

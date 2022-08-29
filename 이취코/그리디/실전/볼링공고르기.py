import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())
K = list(map(int, sys.stdin.readline().rstrip().split()))

balls = []
for i in range(len(K)):
    balls.append([i, K[i]])

answer = 0
for A, B in list(combinations(balls, 2)):
    if A[1] == B[1]:
        continue
    answer += 1

print(answer)
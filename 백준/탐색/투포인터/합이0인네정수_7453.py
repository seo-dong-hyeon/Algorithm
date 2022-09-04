# 합이 0이되는 N개의 정수

import sys

N = int(sys.stdin.readline().rstrip())
A = [0] * N
B = [0] * N
C = [0] * N
D = [0] * N
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, sys.stdin.readline().rstrip().split())

# 특정쌍으로 합이 K가 되는 딕셔너리 조합 만들기
sums = {}
for ai in A:
    for bi in B:
        sums[ai + bi] = sums.get(ai + bi, 0) + 1

# 나머지쌍에서 합이 -K에 대응되는 딕셔너리 개수 확인
answer = 0
for ci in C:
    for di in D:
        answer += sums.get(-(ci + di), 0)

print(answer)

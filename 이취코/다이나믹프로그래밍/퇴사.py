import sys

N = int(sys.stdin.readline().rstrip())
T = []
P = []

for _ in range(N):
    ti, pi = map(int, sys.stdin.readline().rstrip().split())
    T.append(ti)
    P.append(pi)

dp = [0] * (N + 1)
# 0 ~ i 값을 탐색하며 i값을 기준으로 이전 영역을 탐색하며 조건에 맞으면 갱신
for i in range(N):
    if i + T[i] > N:
        continue 
    dp[i] = P[i]
    if i == 0:
        continue
    for j in range(i):
        if T[j] + j <= i:
            dp[i] = max(dp[i], dp[j] + P[i])

print(max(dp))
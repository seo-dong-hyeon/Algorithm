# dp[i][j] = 이전의 올 수 있는 경우들 중 최적의 값 + 현재 값 
import sys

n = int(sys.stdin.readline().rstrip())
triangle = []
dp = [[0] * n for _ in range(n)]
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(len(triangle[i])):
        if i == 0:
            dp[i][0] = triangle[0][0]
            continue
        if j == 0:
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        elif j == len(triangle[i]) - 1:
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

print(max(dp[n - 1]))
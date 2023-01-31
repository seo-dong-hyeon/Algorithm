import sys
from collections import deque


N = int(sys.stdin.readline().rstrip())

maze = []
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().rstrip().split())))

# dp[0] = 가로 방향으로 붙이는 경우의 수
# dp[1] = 세로 방향으로 붙이는 경우의 수
# dp[2] = 대각선 방향으로 붙이는 경우의 수
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue
        if i == 0 and j == 1:
            dp[0][i][j] = 1
            dp[1][i][j] = 0
            dp[2][i][j] = 0
            continue
        if maze[i][j] == 1:
            continue
        # 가로 방향 붙이기 -> 가로 + 대각선 방향 파이브에서 이어붙이기
        if j - 1 >= 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
        # 세로 방향 붙이기 -> 세로 + 대각선 방향 파이브에서 이어붙이기
        if i - 1 >= 0:
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]
        # 대각선 방향 붙이기 -> 가로 + 세로 + 대각선 방향 파이브에서 이어붙이기
        if i - 1 >= 0 and j - 1 >= 0 and maze[i - 1][j] == 0 and maze[i][j - 1] == 0:
            dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1]  + dp[2][i - 1][j - 1] 

print(dp[0][N - 1][N - 1] + dp[1][N - 1][N - 1] + dp[2][N - 1][N - 1])

import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for test_case in range(T):
    N = int(sys.stdin.readline().rstrip())
    maze = [[0] * N for _ in range(N)]
    dp = [[1e9] * N for _ in range(N)]
    for i in range(N):
        row = list(map(int, sys.stdin.readline().rstrip().split()))
        for j in range(N):
            maze[i][j] = row[j]
    dq = deque()
    dp[0][0] = maze[0][0]
    dq.append([0, 0, 0])
    while dq:
        x, y, cost = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if dp[nx][ny] > dp[x][y] + maze[nx][ny]:
                    dp[nx][ny] = dp[x][y] + maze[nx][ny]
                    dq.append([nx, ny, dp[nx][ny]])
    print(dp[N - 1][N - 1])
    
# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4

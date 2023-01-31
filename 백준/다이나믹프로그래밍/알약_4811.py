import sys

max_day = 31
# dp[i][j] = i개의 H와 j개의 W로 만들 수 있는 경우의 수
dp = [[0] * max_day for _ in range(max_day)]

# H 없이 W만 있다면 무조건 W로 만드는 경우밖에 없음
for i in range(1, max_day):
    dp[0][i] = 1

# H가 있으려면 그 전에 H개 이상으로 W를 먹어서 쪼깨놔야함
for h in range(1, max_day):
    for w in range(h, max_day):
        # H를 h 번, W를 w 번 먹은 경우의 수 = 
        # (H를 h - 1 번, W를 w 번 먹은 경우)에서 H를 하나 더 먹는 경우 + 
        # (H를 h 번, W를 w - 1 번 먹은 경우)에서 W를 하나 더 먹는 경우
        dp[h][w] += dp[h - 1][w] + dp[h][w - 1]

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break
    print(dp[N][N])
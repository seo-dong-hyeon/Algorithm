import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))
coins.sort()

# 각 금액별 만들 수 있는 경우의 수
dp = [0] * (k + 1)
for coin in coins:
    # 1원과 2원으로 만드는 경우와 
    # 2원과 1원으로 만드는 경우가 같으므로
    for i in range(coin, k + 1):
        # 만드려는 금액과 동전 금액이 같으면 만드는 경우는 1가지
        if i == coin:
            dp[i] += 1
        # 현재 금액을 만드는 경우의 수 = (현재 금액 - 동전 금액)의 경우의 수 + 동전 금액(1가지) 
        else:
            dp[i] += dp[i - coin]

print(dp[k])

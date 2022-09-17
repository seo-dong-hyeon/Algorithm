# 못생긴 수
import sys

n = int(sys.stdin.readline().rstrip())
dp = [0] * n
dp[0] = 1

# 2,3,5의 배수의 각 인덱스 및 초기값
i2 = i3 = i5 = 0
dp2, dp3, dp5 = 2, 3, 5

for i in range(1, n):
    # 최종 dp에 각 값들 중 최소값을 저장
    dp[i] = min(dp2, dp3, dp5)
    # 어떤 값을 가져왔는지 확인 후
    # 해당 dp의 인덱스 및 값 증가
    if dp[i] == dp2:
        i2 += 1
        dp2 = dp[i2] * 2
    if dp[i] == dp3:
        i3 += 1
        dp3 = dp[i3] * 3
    if dp[i] == dp5:
        i5 += 1
        dp5 = dp[i5] * 5

print(dp[n - 1])

# i2    dp2
# 0     2
# 1     4
# 2     6
# 3     8
# 4     10

# i3    dp3
# 0     3
# 1     6
# 2     9

# i5    dp5
# 0     5
# 1     25

# i     dp
# 0     1
# 1     2
# 2     3
# 3     4
# 4     5
# 5     6
# 6     8

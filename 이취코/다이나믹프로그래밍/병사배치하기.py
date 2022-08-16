import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1] * N

# 가장 긴 증가하는 부분 수열
for i in range(1, N):
    for j in range(i):
        if nums[i] < nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
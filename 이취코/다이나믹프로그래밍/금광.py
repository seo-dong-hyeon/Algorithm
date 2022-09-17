# dp[i][j] = 이전의 올 수 있는 경우들 중 최적의 값 + 현재 값 
import sys

T = int(sys.stdin.readline().rstrip())
for test_case in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    # 1줄 arr -> n행 m열로
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    dp = []
    for i in range(n):
        dp.append(arr[i * m:i * m + m])
    # dp 내려가기 문제
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j - 1]) + dp[i][j]
            elif i == n - 1:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1]) + dp[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1]) + dp[i][j]
    answer = 0
    for i in range(n):
        answer = max(answer, dp[i][m - 1])
    print(answer)

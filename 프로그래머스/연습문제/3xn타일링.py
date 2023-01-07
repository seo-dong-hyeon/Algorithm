def solution(n):
    answer = 0

    dp = [0] * (n + 1)
    dp[1] = 0
    dp[2] = 0
    dp[2] = 3
    dp[3] = 0
    dp[4] = 11
    dp[5] = 0

    # dp[i] = dp[i] * 3 + (dp[i - 4] * 2 + dp[i - 6] * 2 + ...+ dp[2] * 2) + 2
    for i in range(6, n + 1):
        if i % 2 == 0:
            dp[i] += dp[i - 2] * 3
            for j in range(i - 4, -1, -1):
                dp[i] += dp[j] * 2
            dp[i] += 2
            dp[i] = dp[i] % 1000000007
        else:
            dp[i] = 0

    answer = dp[n]

    return answer
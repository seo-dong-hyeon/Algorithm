from collections import deque

def solution(x, y, n):
    answer = 0

    max_num = 1000000
    dp = [1e9] * (max_num + 1)
    
    dq = deque()
    dq.append([x, 0])
    dp[x] = 0
    while dq:
        pos, cost = dq.popleft()
        for i in [pos + n, pos * 2, pos * 3]:
            if i <= y:
                if dp[i] > cost + 1:
                    dp[i] = cost + 1
                    dq.append([i, cost + 1])

    answer = dp[y] if dp[y] != 1e9 else -1

    return answer
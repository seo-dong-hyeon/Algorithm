# 냅색 알고리즘(배낭 문제)
# 도둑의 배낭에 담을 수 있는 무게가 정해져있음 
# 일정 가치와 무게가 있는 짐들을 배낭에 넣을 때
# 가치의 합이 최대가 되도록 짐을 고르는 방법을 찾는 문제

# 0-1 배낭문제
# dp[i][w] = [i번 물건까지 탐색][현재가방 무게 w]에 담을 수 있는 최대 가치
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
W = [0]
V = [0]
for _ in range(N):
    weight, value = map(int, sys.stdin.readline().rstrip().split())
    W.append(weight)
    V.append(value)

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
# 모든 경우에 대해 수행
for i in range(1, N + 1):
    for w in range(1, K + 1):
        weight, value = W[i], V[i]
        # 현재 물건이 현재 돌고있는 무게보다 작다면 [이전 물건까지 탐색][현재가방 무게] 를 입력
        if weight > w:
            dp[i][w] = dp[i - 1][w]
        # [이전 물건까지 탐색][현재가방 무게 - 현재물건 무게] + 현재물건 가치 vs [이전 물건까지 탐색][현재가방 무게]
        # 현재 물건 추가 vs 이전 물건까지 최적값
        else:
            dp[i][w] = max(dp[i - 1][w - weight] + value, dp[i - 1][w])
            
print(dp[N][K])

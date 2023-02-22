import sys
from itertools import permutations

def dfs(i, j, k, cnt):
    # 모든 체력이 0이하면 최소 cnt인지 검사
    if i <= 0 and j <= 0 and k <= 0:
        global answer
        answer = min(answer, cnt)
        return

    # 이미 dp에 저장된 값보다 현재 cnt가 크거나 같다면 탐색 종료 
    if cnt >= dp[i][j][k]:
        return
    dp[i][j][k] = cnt

    # 각 SCV마다 다른 순서로 공격
    for x, y, z in permutations([9, 3, 1], 3):
        dfs(max(i - x, 0), max(j - y, 0), max(k - z, 0), cnt + 1)


N = int(sys.stdin.readline().rstrip())
# SCV 리스트 
# 3개보다 작다면 임의로 체력이 0인 SCV 추가
# 세 개의 공격을 한 번의 cnt로 간주하기 때문에 추가된 체력이 0인 SCV은 그냥 무시해도 됨
SCV = list(map(int, sys.stdin.readline().rstrip().split()))
for _ in range(3 - len(SCV)):
    SCV.append(0)

# dp[i][j][k] = SCV 체력이 i, j, k 일 때, 최소 공격 횟수
dp = [[[1e9 for _ in range(61)] for _ in range(61)] for _ in range(61)]
answer = 1e9
dfs(SCV[0], SCV[1], SCV[2], 0)
print(answer)

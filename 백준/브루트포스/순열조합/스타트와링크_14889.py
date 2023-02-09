import sys
from itertools import combinations

N = int(sys.stdin.readline().rstrip())
S = []
for _ in range(N):
    S.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 사람 번호
nums = [i for i in range(N)]

min_diff = 1e9
# 사람들 중 N / 2 명을 임의로 뽑아서 team1로
for team1 in combinations(nums, N // 2):
    # team1에 안 뽑힌 사람을 team2로
    team2 = [i for i in range(N) if i not in team1]
    # 각각의 능력치 계산 후 차이를 정답과 비교
    power1 = 0
    power2 = 0
    for num1, num2 in combinations(team1, 2):
        power1 += (S[num1][num2] + S[num2][num1])
    for num1, num2 in combinations(team2, 2):
        power2 += (S[num1][num2] + S[num2][num1])
    min_diff = min(min_diff, abs(power1 - power2))

print(min_diff)

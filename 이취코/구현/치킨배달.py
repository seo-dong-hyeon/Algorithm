# N개 중에 M개 선택 문제
# N개 중에 M개 배치 문제
# dfs 선택/선택x 풀이 -> 순열/조합 
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())
maze = [[0] * N for _ in range(N)]
chickens = []
houses = []

for i in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        maze[i][j] = row[j]
        if row[j] == 1:
            houses.append([i, j])
        elif row[j] == 2:
            chickens.append([i, j])

answer = 1e9
for chicken_list in list(combinations(chickens, M)):    # 치킨들 중에 M개를 선택(배치)
    sum_dist = 0
    for house in houses:
        dist = 1e9
        for chicken in chicken_list:
            dist = min(dist, abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
        sum_dist += dist
    answer = min(answer, sum_dist)

print(answer)
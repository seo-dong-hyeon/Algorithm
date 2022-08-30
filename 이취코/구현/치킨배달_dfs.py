import sys

def dfs(idx, cnt):
    # 종료 조건
    if cnt == M:
        totalDist = 0
        for house in houses:
            minDist = 1e9
            for i, chichen in enumerate(chickens):
                if checked[i]:
                    minDist = min(minDist, abs(house[0] - chichen[0]) + abs(house[1] - chichen[1]))
            totalDist += minDist
        global answer
        answer = min(answer, totalDist)
        return
    # 범위 체크
    elif idx >= len(chickens):
        return
    else:
        # 두 갈래길
        # 선택한 것, 안 한 것
        checked[idx] = True
        dfs(idx + 1, cnt + 1)
        checked[idx] = False
        dfs(idx + 1, cnt)
    

N, M = map(int, sys.stdin.readline().rstrip().split())
maze = [[0] * N for _ in range(N)]
chickens = []
houses = []
answer = 1e9

for i in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        maze[i][j] = row[j]
        if row[j] == 1:
            houses.append([i, j])
        elif row[j] == 2:
            chickens.append([i, j])

checked = [False] * len(chickens)

dfs(0, 0)

print(answer)
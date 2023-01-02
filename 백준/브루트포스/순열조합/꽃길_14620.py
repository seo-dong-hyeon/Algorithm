import sys
from itertools import combinations

def bfs(pos):
    cost = 0
    visited = [[False] * N for _ in range(N)]

    for x, y in pos:
        if visited[x][y] == True:
            return -1
        visited[x][y] = True
        cost += flowers[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                visited[nx][ny] = True
                cost += flowers[nx][ny]
            else:
                return -1

    return cost

N = int(sys.stdin.readline().rstrip())

flowers = []
for _ in range(N):
    flowers.append(list(map(int, sys.stdin.readline().rstrip().split())))

poses = []
for i in range(N):
    for j in range(N):
        poses.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 1e9
for pos in list(combinations(poses, 3)):
    cost = bfs(pos)
    if cost != -1:
        answer = min(answer, cost)

print(answer)
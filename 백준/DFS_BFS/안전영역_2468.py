import sys
from collections import deque

def bfs(x, y, height, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    dq.append([x, y])
    visited[x][y] = True

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] > height and visited[nx][ny] is False:
                dq.append([nx, ny])
                visited[nx][ny] = True


N = int(sys.stdin.readline().rstrip())
maze = [[0] * N for _ in range(N)]
max_height = -1

for i in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        maze[i][j] = row[j]
        max_height = max(max_height, maze[i][j])

answer = 1  # 최소 안전영역 개수 = 1
for k in range(1, max_height + 1):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] > k and visited[i][j] is False:
                bfs(i, j, k, visited)
                cnt += 1
    answer = max(answer, cnt)

print(answer)

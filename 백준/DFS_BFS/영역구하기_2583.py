import sys
from collections import deque

def bfs(x, y, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    dq.append([x, y])
    visited[x][y] = True
    area = 1

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and maze[nx][ny] is False and visited[nx][ny] is False:
                dq.append([nx, ny])
                visited[nx][ny] = True
                area += 1

    return area


M, N, K = map(int, sys.stdin.readline().rstrip().split())
maze = [[False] * N for _ in range(M)]

# 왼쪽 아래
# 0, 2 -> 2, 0
# 1, 1 -> 3, 1
# 4, 0 -> 4, 4
# x, y -> M - y - 1, x

# 오른쪽 아래
# 4, 4 -> 1, 3
# 2, 5 -> 0, 1
# 6, 2 -> 3, 5
# x, y -> M - y, x - 1
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    x1, y1, x2, y2 = M - y1 - 1, x1, M - y2, x2 - 1
    sx = min(x1, x2)
    sy = min(y1, y2)
    ex = max(x1, x2)
    ey = max(y1, y2)
    for i in range(sx, ex + 1):
        for j in range(sy, ey + 1):
            maze[i][j] = True

visited = [[False] * N for _ in range(M)]
cnt = 0
areas = []
for i in range(M):
    for j in range(N):
        if maze[i][j] is False and visited[i][j] is False:
            areas.append(bfs(i, j, visited))
            cnt += 1
areas.sort()

print(cnt)
print(" ".join(list(map(str, areas))))

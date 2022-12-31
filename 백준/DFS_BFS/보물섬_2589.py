import sys
from collections import deque

def bfs(x, y):
    global answer

    checked = [[False] * M for _ in range(N)]
    checked[x][y] = True

    dq = deque()
    # x좌표, y좌표, 기준점으로부터 거리
    dq.append([x, y, 0])
    while dq:
        x, y, cnt = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 'L' and checked[nx][ny] is False:
                dq.append([nx, ny, cnt + 1])
                checked[nx][ny] = True
                answer = max(answer, cnt + 1)


N, M = map(int, sys.stdin.readline().rstrip().split())
maze = []
for _ in range(N):
    maze.append(sys.stdin.readline().rstrip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

for i in range(N):
    for j in range(M):
        # 육지인 좌표에 대하여 브루트포스
        if maze[i][j] == 'L':
            bfs(i, j)

print(answer)
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
maze = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

viruses = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(row)):
        if row[j] != 0:
            viruses.append([row[j], i, j, 0])
    maze.append(row)

S, X, Y = map(int, sys.stdin.readline().rstrip().split())

viruses.sort()
dq = deque()
for virus in viruses:
    dq.append(virus)

times = [[0] * N for _ in range(N)]
while dq:
    num, x, y, time = dq.popleft()
    if time >= S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N and maze[nx][ny] == 0:
            maze[nx][ny] = num
            dq.append([num, nx, ny, time + 1])

print(maze[X - 1][Y - 1])

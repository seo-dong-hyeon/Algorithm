import sys
from collections import deque

R, C = map(int, sys.stdin.readline().rstrip().split())
maze = [[0] * C for _ in range(R)]
fired = [[0] * C for _ in range(R)]
for i in range(R):
    row = sys.stdin.readline().rstrip()
    for j in range(C):
        maze[i][j] = row[j]

# 지훈이, 불들 위치 저장
J = []
fires = []
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            J = [i, j]
        elif maze[i][j] == 'F':
            fires.append([i, j])

# 불들이 퍼지는 시간 저장
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dq = deque()
for fire in fires:
    dq.append([fire[0], fire[1], 1])
    fired[fire[0]][fire[1]] = 1
while dq:
    x, y, cnt = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] != '#' and fired[nx][ny] == 0:
            dq.append([nx, ny, cnt + 1])
            fired[nx][ny] = cnt + 1

# 지훈이 탈출
dq.append([J[0], J[1], 1])
maze[J[0]][J[1]] = 1
answer = 0
while dq:
    x, y, cnt = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            # 벽이 아니면서 불이 퍼지지 않았거나 불이 퍼진 시간보다 빨리 왔으면 이동
            if maze[nx][ny] == '.' and (fired[nx][ny] == 0 or fired[nx][ny] > cnt + 1):
                dq.append([nx, ny, cnt + 1])
                maze[nx][ny] = cnt + 1
        # 범위 밖으로 벗어나면 탈출 성공
        else:
            answer = cnt + 1
            break
    if answer:
        break

print(answer - 1 if answer else "IMPOSSIBLE")
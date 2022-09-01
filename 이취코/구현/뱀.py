import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

maze = [[0] * N for _ in range(N)]
for i in range(K):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    maze[r - 1][c - 1] = 2

L = int(sys.stdin.readline().rstrip())
turns = deque()     # 이동 정보
for _ in range(L):
    X, C = sys.stdin.readline().rstrip().split()
    turns.append([int(X), C])

maze[0][0] = 1
direction = 1       # 0 1 2 3 (상 우 하 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
tails = deque()     # 꼬리 위치좌표 정보 큐
tails.append([0, 0])
x = 0
y = 0

time = 0
while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx < 0 or nx >= N or ny < 0 or ny >= N or maze[nx][ny] == 1:
        break
    # 이동한 좌표에 사과가 없다면 
    # 가장 마지막 위치의 꼬리가 줄어들고
    # 새로 이동하는 좌표를 꼬리에 추가
    if maze[nx][ny] != 2:
        bx, by = tails.popleft()
        maze[bx][by] = 0
    maze[nx][ny] = 1
    tails.append([nx, ny])
    x = nx
    y = ny
    
    time += 1
    # 방향 변환
    if len(turns) > 0 and time == turns[0][0]:
        if turns[0][1] == 'L':
            direction = direction - 1 if direction - 1 >= 0 else 3
        else:
            direction = (direction + 1) % 4
        turns.popleft() 

print(time + 1)
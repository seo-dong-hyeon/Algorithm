import sys 
from collections import deque

# 가장 가까운 물고기 거리, 위치 구하기
def bfs(x, y):
    dq = deque()
    distances = [[1e9] * N for _ in range(N)]
    dq.append([x, y, 0])
    distances[x][y] = 0
    # maze 상에서 각각의 위치에 최단거리 구하기
    while dq:
        x, y, dist = dq.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N and distances[nx][ny] > dist + 1 and shark_size >= maze[nx][ny]:
                dq.append([nx, ny, dist + 1])
                distances[nx][ny] = dist + 1

    # 가장 가까운 물고기 중에 가장 왼쪽에 있는 물고기의 거리, 위치 구하기
    min_dist = 1e9
    min_pos = [0, 0]
    for fish in fishes:
        x, y = fish
        if maze[x][y] == shark_size:    # 같은 크기 물고기는 못 먹음
            continue
        if min_dist > distances[x][y]:
            min_dist = distances[x][y]
            min_pos = [x, y]
        elif min_dist == distances[x][y]:
            if min_pos[0] > x:
                min_dist = distances[x][y]
                min_pos = [x, y]
            elif min_pos == x:
                if min_pos[1] > y:
                    min_dist = distances[x][y]
                    min_pos = [x, y]

    if min_dist == 1e9 and min_pos[0] == 0 and min_pos[1] == 0: # 한 마리도 못 먹으면 -1 리턴
        return -1, min_pos
    
    return min_dist, min_pos
    

N = int(sys.stdin.readline().rstrip())
maze = []
fishes = []
shark_size = 2
eated = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x = 0
y = 0

for i in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    maze.append(row)
    for j in range(len(row)):
        if row[j] == 9:
            x = i
            y = j
        elif row[j] != 0:
            fishes.append([i, j])

answer = 0
while len(fishes):
    min_dist, min_pos = bfs(x, y)
    if min_dist == -1:  # 한 마리도 못 먹으면 종료
        break
    answer += min_dist
    eated += 1
    if eated == shark_size: # 먹은 물고기 수가 상어 크기와 같다면 크기 증가
        shark_size += 1
        eated = 0
    # 기존 상어 위치 0으로
    # 현재 상어 위치 잡아먹은 물고기 위치로
    # 잡아먹은 물고기는 리스트에서 제외
    maze[x][y] = 0
    x, y = min_pos[0], min_pos[1]
    fishes.remove(min_pos)

print(answer)

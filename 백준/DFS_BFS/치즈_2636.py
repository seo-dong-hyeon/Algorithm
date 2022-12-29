import sys
from collections import deque

# 전체 치즈 개수
cheeseCnt = 0
r, c = map(int, sys.stdin.readline().rstrip().split())
maze = []
for _ in range(r):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in row:
        if i == 1:
            cheeseCnt += 1
    maze.append(row)

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]
loopCnt = 0
# 이전 단계 치즈 개수
beforeCnt = cheeseCnt
while cheeseCnt:
    beforeCnt = cheeseCnt
    # 방문 여부
    visited = [[False] * c for _ in range(r)]
    dq = deque()
    dq.append([0, 0])
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < r and ny >= 0 and ny < c:
                # 아직 방문 안한 치즈면 방문 표시하고 녹임
                if maze[nx][ny] == 1 and not visited[nx][ny]:
                    maze[nx][ny] = 0
                    visited[nx][ny] = True
                    cheeseCnt -= 1
                # 아직 방문 안한 그냥 자리면 방문 표시하고 이동
                elif maze[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dq.append([nx, ny])
    loopCnt += 1

print(loopCnt)
print(beforeCnt)
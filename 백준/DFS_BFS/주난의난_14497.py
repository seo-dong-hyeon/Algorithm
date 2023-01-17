import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

maze = []
for _ in range(N):
    maze.append(sys.stdin.readline().rstrip())
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
dq = deque()
dq.append([x1, y1, 1])
while dq:
    x, y, cnt = dq.popleft()
    if x == x2 and y == y2:
        answer = cnt
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            # 아직 방문안한 친구면 카운트 증가
            # 실제론 새로 점프하는 것이지만
            # queue에 일괄적으로 넣으므로 카운트만 증가
            if maze[nx][ny] == '1' and visited[nx][ny] is False:
                dq.append([nx, ny, cnt + 1])
                visited[nx][ny] = True
            # 아직 방문안한 빈 공간이면 우선적으로 넣음
            # 해당 바람은 친구를 만난 이후에 카운트만 증가시키고 뻗어나가는(실제론 새로 점프) 
            # queue 원소보다 우선해야 함
            elif maze[nx][ny] != '*' and visited[nx][ny] is False:
                dq.appendleft([nx, ny, cnt])
                visited[nx][ny] = True

print(answer)
import sys
from collections import deque

def bfs(x, y, section):
    dq = deque()
    dq.append([x, y])
    visited[x][y] = section
    ppl = 0     # 칸들의 모든 인구수 합
    cnt = 0     # 칸들의 개수

    while len(dq):
        x, y = dq.popleft()
        ppl += A[x][y]  # 해당 칸의 인구수 더함
        cnt += 1        # 칸 개수 증가
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 아직 방문하지 않고 차이가 범위 이내라면 
            # 해당 섹션으로 분류
            if nx >= 0 and nx < N and ny >= 0 and ny < N and visited[nx][ny] == 0:
                diff = abs(A[nx][ny] - A[x][y])
                if diff >= L and diff <= R:
                    visited[nx][ny] = section
                    dq.append([nx, ny])

    # 모든 인구수 합 / 칸 개수
    return int(ppl / cnt)


N, L, R = map(int, sys.stdin.readline().rstrip().split())
A = []
visited = [[0] * N for _ in range(N)]   # visited[x][y] = (x, y) 칸의 섹션(분류)

for i in range(N):
    A.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = 0
while True:
    section = 1
    unionPpl = [0]      # unionPpl[section] = 이동 후 각 칸의 인구수
    totalCnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                unionPpl.append(bfs(i, j, section))
                totalCnt += 1
                section += 1

    # 국경이 안 열렸으면 종료
    if totalCnt == N * N:
        break

    # 새로운 칸의 인구
    # (x, y) -> visited -> 해당 칸의 section
    # section -> unionPpl -> 이동 후 각 칸의 인구수 가져옴
    # visited 초기화
    # 인구 이동날 증가
    for i in range(N):
        for j in range(N):
            A[i][j] = unionPpl[visited[i][j]]
            visited[i][j] = 0
    answer += 1

print(answer)
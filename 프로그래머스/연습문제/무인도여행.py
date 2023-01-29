from collections import deque

def bfs(maps, visited, x, y, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0,0, -1, 1]
    cnt = 0

    dq = deque()
    dq.append([x, y])
    visited[x][y] = True
    while dq:
        x, y = dq.popleft()
        cnt += int(maps[x][y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != 'X' and visited[nx][ny] is False:
                dq.append([nx, ny])
                visited[nx][ny] = True

    return cnt

def solution(maps):
    answer = []

    N = len(maps)
    M = len(maps[0])
    visited = [[False] * (M + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X' and visited[i][j] is False:
                answer.append(bfs(maps, visited, i, j, N, M))

    if len(answer):
        answer.sort()
    else:
        answer.append(-1)

    return answer

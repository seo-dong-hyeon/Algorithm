from collections import deque

def bfs(maps, x_start, y_start, x_end, y_end):
    N = len(maps)
    M = len(maps[0])
    visited = [[1e9] * (M + 1) for _ in range(N + 1)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dq = deque()
    dq.append([x_start, y_start, 0])
    while dq:
        x, y, cost = dq.popleft()
        if x == x_end and y == y_end:
            return cost
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != 'X' and visited[nx][ny] > cost + 1:
                dq.append([nx, ny, cost + 1])
                visited[nx][ny] = cost + 1

    return visited[x_end][y_end]


def solution(maps):
    answer = 0

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                S = [i, j]
            elif maps[i][j] == 'E':
                E = [i, j]
            elif maps[i][j] == 'L':
                L = [i, j]
    
    cost1 = bfs(maps, S[0], S[1], L[0], L[1])
    if cost1 == 1e9:
        return -1
    cost2 = bfs(maps, L[0], L[1], E[0], E[1])
    if cost2 == 1e9:
        return -1
        
    answer = cost1 + cost2

    return answer
import sys

def dfs(x, y, visited, dist):
    if dist == K:
        if x == 0 and y == C - 1:
            global answer
            answer += 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] != 'T' and visited[nx][ny] is False:
            visited[nx][ny] = True
            dfs(nx, ny, visited, dist + 1)
            visited[nx][ny] = False


R, C, K = map(int, sys.stdin.readline().rstrip().split())

maze = []
for _ in range(R):
    maze.append(sys.stdin.readline().rstrip())

visited = [[False] * C for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

visited[R - 1][0] = True
dfs(R - 1, 0, visited, 1)

print(answer)

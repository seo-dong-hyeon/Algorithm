R, C = map(int, input().split())
maze = [[1e9 for _ in range(C)] for _ in range(R)]
checked = [[1e9 for _ in range(C)] for _ in range(R)] 
D = []
S = []
waters = []
for i in range(R): 
    column = input()
    for j in range(C):
        if column[j] == '*':
            waters.append([i, j, 0])
            maze[i][j] = 0
        elif column[j] == 'D':
            D.append([i, j])
            maze[i][j] = -2
        elif column[j] == 'S':
            S.append([i, j, 0])
            checked[i][j] = 0
        elif column[j] == 'X':
            maze[i][j] = -1

# 물이 찰 시간을 미리 계산
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while len(waters) != 0:
    x, y, cnt = waters.pop(0)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if maze[nx][ny] > cnt + 1:
            maze[nx][ny] = cnt + 1
            waters.append([nx, ny, cnt + 1])

flag = False
minDist = 1e9
while len(S) != 0:
    x, y, cnt = S.pop(0)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if maze[nx][ny] > cnt + 1 and checked[nx][ny] > cnt + 1:
            S.append([nx, ny, cnt + 1])
            checked[nx][ny] = cnt + 1
        if nx == D[0][0] and ny == D[0][1]:
            flag = True
            minDist = min(minDist, cnt + 1)

print(minDist if flag else "KAKTUS")
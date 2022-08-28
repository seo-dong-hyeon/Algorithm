import sys
import copy

answer = 0
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def move(maze, fishes, shark):
    # 물고기 이동
    for i in range(len(fishes)):
        a, b, x, y, eated = fishes[i]
        if eated:
            continue
        while True:
            nx = x + dx[b - 1]
            ny = y + dy[b - 1]
            if nx >= 0 and nx < 4 and ny >= 0 and ny < 4 and not (nx == shark[0] and ny == shark[1]):
                # 기준 물고기 방향, 좌표 변경
                fishes[a][1] = b
                fishes[a][2] = nx
                fishes[a][3] = ny
                # 위치를 변경하는 물고기 좌표 변경
                fishes[maze[nx][ny][0]][2] = x
                fishes[maze[nx][ny][0]][3] = y
                # 방향 변경 후 지도상 위치 변경
                maze[x][y][1] = b
                maze[x][y], maze[nx][ny] = maze[nx][ny], maze[x][y]
                break
            b = (b + 1) % 8

    return maze, fishes


def dfs(maze, fishes, x, y, eated):
    a = maze[x][y][0]   # 이동한 위치의 물고기 번호
    b = maze[x][y][1]   # 이동한 위치의 물고기 방향
    eated += a          # 물고기 먹음
    shark = [x, y, b]   # 상어 정보를 물고기 좌표와 방향으로 변경
    fishes[a][4] = True # 해당 물고기 잡아먹힘
    global answer
    answer = max(answer, eated) # 최대값 갱신
    
    # 물고기 이동
    maze, fishes = move(maze, fishes, shark)

    # 상어 이동
    for _ in range(4):
        x += dx[b - 1]
        y += dy[b - 1]
        if x >= 0 and x < 4 and y >= 0 and y < 4 and fishes[maze[x][y][0]][4] == False:
            # 이동 가능하다면 해당 좌표로 이동
            # 모든 경우의 수 고려
            dfs(copy.deepcopy(maze), copy.deepcopy(fishes), x, y, eated)
    return

cnt = 0
maze = []
fishes = [[0, 0, 0, 0, True]]   # 인덱스 맞추기
for i in range(4):
    a0, b0, a1, b1, a2, b2, a3, b3 = map(int, sys.stdin.readline().rstrip().split())
    # maze[i][j] = (i, j)의 [번호, 좌표]
    # fishes[i]  = i번 물고기의 [번호, 방향, x좌표, y좌표, 잡아먹혔는지 여부]
    maze.append([[a0, b0], [a1, b1], [a2, b2], [a3, b3]])
    fishes.append([a0, b0, i, 0, False])
    fishes.append([a1, b1, i, 1, False])
    fishes.append([a2, b2, i, 2, False])
    fishes.append([a3, b3, i, 3, False])
fishes.sort()

dfs(maze, fishes, 0, 0, 0)

print(answer)

import sys

def move_dust(maze):
    tmp = [[0 for _ in range(C + 1)] for _ in range(R + 1)]

    # 확산된 먼지들
    for x in range(R):
        for y in range(C):
            if maze[x][y][0] > 0:
                dust = maze[x][y].pop()
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < R and 0 <= ny < C and maze[nx][ny][0] != -1:
                        tmp[nx][ny] += dust // 5
                        cnt += 1
                maze[x][y].append(dust - (dust // 5) * cnt)

    # 기존 먼지들에 더함
    for x in range(R):
        for y in range(C):
            maze[x][y][0] += tmp[x][y]


def clean_dust(maze):
    for i, pos in enumerate(cleaner):
        x, y = pos
        # 공기정청기가 있는 칸은 먼지가 없기 때문에 다음 칸부터
        y += 1

        # 오른쪽 이동
        while True:
            if y == C - 1:
                break
            maze[x][y + 1].append(maze[x][y].pop(0))
            if len(maze[x][y]) == 0:
                maze[x][y].append(0)
            y += 1

        # 위로 이동
        if i == 0:
            while True:
                if x == 0:
                    break
                maze[x - 1][y].append(maze[x][y].pop(0))
                x -= 1
        # 아래로 이동
        else:
            while True:
                if x == R - 1:
                    break
                maze[x + 1][y].append(maze[x][y].pop(0))
                x += 1

        # 왼쪽 이동
        while True:
            if y == 0:
                break
            maze[x][y - 1].append(maze[x][y].pop(0))
            y -= 1

        # 위로 이동
        if i == 1:
            while True:
                if maze[x][y][0] == -1:
                    break
                maze[x - 1][y].append(maze[x][y].pop(0))
                x -= 1
        # 아래로 이동
        else:
            while True:
                if maze[x][y][0] == -1:
                    break
                maze[x + 1][y].append(maze[x][y].pop(0))
                x += 1


R, C, T = map(int, sys.stdin.readline().rstrip().split())
maze = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
cleaner = []

for i in range(R):
    rows = list(map(int, sys.stdin.readline().rstrip().split()))
    for j, row in enumerate(rows):
        maze[i][j].append(row)
        if row == -1:
            cleaner.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(T):
    # 먼지확산
    move_dust(maze)
    # 공기청정기 작동
    clean_dust(maze)

answer = 0
for x in range(R):
    for y in range(C):
        answer += (maze[x][y][0] if maze[x][y][0] != -1 else 0)
print(answer)
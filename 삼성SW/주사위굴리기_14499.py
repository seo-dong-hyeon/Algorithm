N, M, x, y, K = map(int, input().split())

maze = [[0] * (M  + 1) for _ in range(N + 1)]

for i in range(N):
    rows = list(map(int, input().split()))
    for j in range(M):
        maze[i][j] = rows[j]

ops = list(map(int, input().split()))

# 주사위 값
# dice[i] = 주사위의 위치 i의 값
dice = [0] * 7
# 현재 주사위 위치별 인덱스
middle = 1
left = 4
right = 3
up = 2
down = 5
cross = 6

# 동서북남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for op in ops:
    nx = x + dx[op]
    ny = y + dy[op]
    if nx >= 0 and nx < N and ny >= 0 and ny < M:
        x = nx
        y = ny
        if op == 1:
            left, middle, right, cross = middle, right, cross, left
            #   2
            # 4 1 3
            #   5
            #   6
            ########
            #   2
            # 1 3 6
            #   5
            #   4
        elif op == 2:
            left, middle, right, cross = cross, left, middle, right
            #   2
            # 4 1 3
            #   5
            #   6
            ########
            #   2
            # 6 4 1
            #   5
            #   3
        elif op == 3:
            up, middle, down, cross = cross, up, middle, down
            #   2
            # 4 1 3
            #   5
            #   6
            ########
            #   6
            # 4 2 3
            #   1
            #   5
        else:
            up, middle, down, cross = middle, down, cross, up
            #   2
            # 4 1 3
            #   5
            #   6
            ########
            #   1
            # 4 5 3
            #   6
            #   2
        if maze[x][y] == 0:
            maze[x][y] = dice[middle]
        else:
            dice[middle] = maze[x][y]
            maze[x][y] = 0
            
        print(dice[cross])

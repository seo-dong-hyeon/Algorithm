N, M, K = map(int, input().split())

maze = []
sharks = [[] * (M + 1) for _ in range(M + 1)]   # 상어 리스트, sharks[i] = i번 상어의 현재 위치
maze_smell = []                                 # 냄새 격자 [상어 번호, 남은 시간]
alive = [True] * (M + 1)                        # i번 상어의 생존 유무
alive[0] = False                                # 0번 상어는 없으므로 죽이고 시작
# 상어 위치 저장 후 해당 위치에 냄새를 뿌림
for i in range(N):
    row = list(map(int, input().split()))
    rows = []
    maze.append(row)
    for j in range(len(row)):
        if row[j] != 0:
            sharks[row[j]] = [i, j]
        rows.append([row[j], K if row[j] != 0 else 0])
    maze_smell.append(rows)

# i번 상어의 현재 방향
directions = {}
for idx, direction in enumerate(list(map(int, input().split()))):
    directions[idx + 1] = direction

# i번 상어의 방향에 따른 우선순위
direction_prior = {}
for i in range(1, M + 1):
    direction_prior[i] = {}
    for j in range(1, 5):
        direction_prior[i][j] = list(map(int, input().split()))

# 위, 아래, 왼쪽, 오른쪽
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
time = 0
while time <= 1000:
    cnt = 0
    for num in range(M + 1):
        # 상어가 죽었으면 넘어감
        if alive[num] == False:
            continue
        x, y = sharks[num]
        cnt += 1
        possible = []
        # 인접한 칸들 중 냄새가 없는 칸을 탐색
        for i in range(1, 5):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N and maze_smell[nx][ny][0] == 0:
                possible.append([nx, ny, i])
        # 이동 가능한 칸이 없거나 1개 이상이면
        if len(possible) != 1:
            # 이동 가능한 칸이 없다면
            if len(possible) == 0:
                # 인접한 칸에서 자기 냄새가 있는 칸들을 가져옴
                for i in range(1, 5):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= 0 and nx < N and ny >= 0 and ny < N and maze_smell[nx][ny][0] == num:
                        possible.append([nx, ny, i])
            now_direction = directions[num]                     # 현재 상어 방향
            priotities = direction_prior[num][now_direction]    # 현재 방향에 따른 이동 방향 우선순위
            # 이동 가능한 방향 중에서
            # 현재 방향에 따른 우선순위가 가장 높은 방향을 정함
            min_idx = 100
            max_priority = 0
            for j in range(len(possible)):
                for idx, priority in enumerate(priotities):
                    if possible[j][2] == priority and min_idx > idx:
                        min_idx = idx
                        max_priority = priority
            direction = max_priority
            nx = x + dx[direction]
            ny = y + dy[direction]
        # 이동 가능한 칸이 1개면 해당 칸을 이동할 칸으로 결정
        else:
            nx, ny, direction = possible[0]

        # 이동할 칸에 상어가 없으면 바로 이동
        if maze[nx][ny] == 0:
            maze[nx][ny] = num
        # 이동할 칸에 상어가 있다면 더 작은 수의 상어가 살아남음
        else:
            if maze[nx][ny] > num:
                maze[nx][ny] = num
                alive[maze[nx][ny]] = False
            else:
                alive[num] = False
        # 상어 위치, 방향 변경
        sharks[num] = [nx, ny]
        directions[num] = direction
        # 기존 상어 위치는 제거
        maze[x][y] = 0

    # 한 마리만 남아 있으면 종료
    if cnt == 1:
        break

    # 남은 냄새시간을 줄임
    for i in range(N):
        for j in range(N):
            num, rest_time = maze_smell[i][j]
            if num != 0:
                rest_time -= 1
                # 남은 시간이 0이면 해당 냄새는 사라짐
                if rest_time == 0:
                    num = 0
            maze_smell[i][j][0] = num
            maze_smell[i][j][1] = rest_time

    # 상어가 현재있는 곳에 냄새를 뿌림
    for num in range(M + 1):
        if alive[num] == False:
            continue
        x, y = sharks[num]
        maze_smell[x][y][0] = num
        maze_smell[x][y][1] = K
        
    time += 1
       
print(time if time != 1001 else -1)

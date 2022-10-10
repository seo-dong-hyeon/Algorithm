from collections import deque

def move_dice(dice, x, y, d):
    global N, M, dx, dy
    # 방향이 벗어나면 반대 반향으로
    if not (0 <= x + dx[d] < N and 0 <= y + dy[d] < M):
        if d == 0:
            d = 2
        elif d == 1:
            d = 3
        elif d == 2:
            d = 0
        else:
            d = 1

    # 주사위 이동
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < N and 0 <= ny < M:
        # 동쪽 이동
        if d == 0:
            dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
            #   2
            # 4 1 3
            #   5
            #   6
            ########
            #   2
            # 6 4 1
            #   5
            #   3
        # 남쪽 이동
        elif d == 1:
            dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
            #   2
            # 4 1 3
            #   5
            #   6
            ########
            #   6
            # 4 5 3
            #   1
            #   2
        # 서쪽 이동
        elif d == 2:
            dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
            #   2
            # 4 1 3
            #   5
            #   6
            ########
            #   2
            # 1 3 6
            #   5
            #   4
        # 북쪽 이동
        else:
            dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
            #   2
            # 4 1 3
            #   5
            #   6
            ########
            #   1
            # 4 5 3
            #   6
            #   2

    return dice, [nx, ny], d


def rotate_direction(num, x, y, d):
    global maze
    # 90도 시계방향 회전
    if num > maze[x][y]:
        d = (d + 1) % 4
    # 90도 반시계방향 회전
    elif num < maze[x][y]:
        d -= 1
        if d == -1:
            d = 3

    return d


def count_score(x, y, d):
    global N, M, maze, dx, dy
    B = maze[x][y]
    C = 1
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    dq = deque()
    dq.append([x, y])
    visited[x][y] = True

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == B and visited[nx][ny] is False:
                visited[nx][ny] = True
                dq.append([nx, ny])
                C += 1

    return B * C


N, M, K = map(int, input().split())
maze = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        maze[i][j] = row[j]

# 주사위 위치별 숫자
dice = [2, 4, 1, 3, 5, 6]
# 현재 주사위 위치별 인덱스

# 방향
# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0

# 이동 시작
answer = 0
dice_pos = [0, 0]
for _ in range(K):
    # 주사위 굴리기
    dice, dice_pos, d = move_dice(dice, dice_pos[0], dice_pos[1], d)
    x, y = dice_pos

    # 방향 결정
    d = rotate_direction(dice[5], dice_pos[0], dice_pos[1], d)

    # 점수 구하기
    answer += count_score(dice_pos[0], dice_pos[1], d)

print(answer)

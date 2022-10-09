import copy

def move_fish(maze):
    global shark_pos, smell
    # 물고기 이동
    #        좌 좌위 위 우위 우 우하 하 좌하
    dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

    # 이동한 물고기 위치 리스트
    result = [[[] for _ in range(5)] for _ in range(5)]

    for x in range(1, 5):
        for y in range(1, 5):
            # 해당 칸에 물고기가 있을때까지
            while maze[x][y]:
                d = maze[x][y].pop()
                # 이동 여부
                flag = False
                # 현재 방향 + 안되면 반시계로 회전하면서
                for _ in range(8):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    # 범위에 있거나 상어가 없거나 냄새가 없으면 이동
                    if 1 <= nx <= 4 and 1 <= ny <= 4 and not (nx == shark_pos[0] and ny == shark_pos[1]) and smell[nx][ny] == 0:
                        result[nx][ny].append(d)
                        flag = True
                        break
                    # 아니면 반시계 회전
                    else:
                        d -= 1
                        if d == 0:
                            d = 8
                # 이동할 곳이 없다면 그냥 현재 위치에
                if not flag:
                    result[x][y].append(d)

    return result


def move_shark(x, y, depth, eat_cnt, visit, paths):
    if depth == 3:
        global max_eat, shark_pos, max_path
        if eat_cnt > max_eat:
            max_eat = eat_cnt
            shark_pos = [x, y]
            max_path = copy.deepcopy(paths)
        return

    # 상어 이동
    #       상 좌 하 우
    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, -1, 0, 1]
    
    # 상좌하우로 이동하면서
    for d in range(1, 5):
        nx = x + dx[d]
        ny = y + dy[d]
        # 범위에 있다면
        if 1 <= nx <= 4 and 1 <= ny <= 4:
            # 처음 방문하는 곳이면
            if visit[nx][ny] is False:
                # 방문 표시
                visit[nx][ny] = True
                # 해당 경로 저장
                paths.append([nx, ny])
                # 해당 위치의 물고기를 먹고 이동
                move_shark(nx, ny, depth + 1, eat_cnt + len(maze[nx][ny]), visit, paths)
                visit[nx][ny] = False
                paths.pop()
            # 이미 방문한 곳이면
            else:
                # 횟수만 증가
                move_shark(nx, ny, depth + 1, eat_cnt, visit, paths)


M, S = map(int, input().split())
maze = [[[] for _ in range(5)] for _ in range(5)]   # maze[i][j] = [...] 해당 칸의 물고기 방향
smell = [[0] * 6 for _ in range(6)]                 # 해당 칸의 냄새

# 물고기 위치 저장
for _ in range(M):
    x, y, d = map(int, input().split())
    maze[x][y].append(d)

# 상어 위치
x, y = map(int, input().split())
shark_pos = [x, y]

# 마법 연습
for idx in range(S):
    # 1단계 - 물고기 복사
    tmp_maze = copy.deepcopy(maze)

    # 2단계 - 물고기 이동
    maze = move_fish(maze)

    # 3단계 - 상어 이동
    max_eat = -1                                # 최대로 많이 먹은 물고기 수
    max_path = []                               # 최대로 물고기를 많이 먹는 경로
    visited = [[False] * 6 for _ in range(6)]   # 해당 칸 방문 여부
    move_shark(shark_pos[0], shark_pos[1], 0, 0, visited, [])
    # 상어가 이동하면서 
    # 물고기가 있다면 다 먹고
    # 냄새를 남김
    for x, y in max_path:
        if maze[x][y]:
            maze[x][y] = []
            smell[x][y] = 3

    # 4단계 - 냄새 없애기
    for i in range(1, 5):
        for j in range(1, 5):
            if smell[i][j] > 0:
                smell[i][j] -= 1

    # 5단계 - 물고기 붙여넣기
    for i in range(1, 5):
        for j in range(1, 5):
            maze[i][j] += tmp_maze[i][j]

# 물고기 수 세기
answer = 0
for i in range(1, 5):
    for j in range(1, 5):
        if len(maze[i][j]) > 0:
            answer += len(maze[i][j])

print(answer)

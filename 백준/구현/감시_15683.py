import copy

def check(maze_direction):
    global max_cnt
    visited = copy.deepcopy(maze_state)
    cnt = 0
    # 모든 cctv에 대해
    for num, x, y in cctv_list:
        direction = maze_direction[x][y][0]
        # 해당 위치에서 감시할 수 있는 방향들을 가져와서 좌표를 벗어나거나 벽을 만날때까지 진행
        for dx, dy in direction:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != 6:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = "#"
                        cnt += 1
                else:
                    break
    max_cnt = max(max_cnt, cnt)


def dfs(cctv_idx, maze_direction):
    # 모든 cctv를 탐색했으면 감시 시작
    if cctv_idx == len(cctv_list):
        check(maze_direction)
        return
    # cctv 하나를 가져옴
    num, x, y = cctv_list[cctv_idx]
    for direction in direction_list[num - 1]:
        # 해당 cctv가 감시할 수 있는 방향들을 가져와서 저장
        maze_direction[x][y].append(direction)
        dfs(cctv_idx + 1, maze_direction)
        maze_direction[x][y].pop()


import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

# 사무실 정보
maze_state = []
cctv_list = []
empty_cnt = 0
for i in range(N):
    rows = list(map(int, sys.stdin.readline().rstrip().split()))
    for j, row in enumerate(rows):
        if row == 0:
            empty_cnt += 1
        elif 1 <= row <= 5:
            cctv_list.append([row, i, j])
    maze_state.append(rows)

# 각 위치별 감시할 수 있는 방향들 저장
maze_direction = [[[] for _ in range(M)] for _ in range(N)]

# 각 cctv 별 감시할 수 있는 방향들
direction_list = [[[[-1, 0]], [[1, 0]], [[0, -1]], [[0, 1]]],
                  [[[-1, 0], [1, 0]], [[0, -1], [0, 1]]],
                  [[[-1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 0], [0, -1]], [[0, -1], [-1, 0]]],
                  [[[1, 0], [0, -1], [0, 1]], [[-1, 0], [0, -1], [0, 1]], [[-1, 0], [1, 0], [0, 1]], [[-1, 0], [1, 0], [0, -1]]],
                  [[[-1, 0], [1, 0], [0, -1], [0, 1]]]]

max_cnt = 0
dfs(0, maze_direction)
print(empty_cnt - max_cnt)

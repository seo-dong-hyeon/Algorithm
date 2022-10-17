def get_adjacent_cnt(num, x, y):
    global N, maze, loves
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    adjacent_cnt = 0
    vacant_cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if maze[nx][ny] in loves[num]:
                adjacent_cnt += 1
            elif maze[nx][ny] == 0:
                vacant_cnt += 1

    return adjacent_cnt, vacant_cnt


def get_satisfaction(num, x, y):
    global N, maze, loves
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    adjacent_cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if maze[nx][ny] in loves[num]:
                adjacent_cnt += 1

    satisfaction = 0
    if adjacent_cnt == 1:
        satisfaction = 1
    elif adjacent_cnt == 2:
        satisfaction = 10
    elif adjacent_cnt == 3:
        satisfaction = 100
    elif adjacent_cnt == 4:
        satisfaction = 1000

    return satisfaction


N = int(input())
maze = [[0] * N for _ in range(N)]
loves = [[] for _ in range(N * N + 1)]

student_order = []
for _ in range(N * N):
    students = list(map(int, input().split()))
    loves[students[0]] = students[1:]
    student_order.append(students[0])

for num in student_order:
    max_adjacent_cnt = -1
    max_vacant_cnt = -1
    max_idx = [-1, -1]
    for i in range(N):
        for j in range(N):
            # 좋아하는 학생이 가장 인접하면서 빈 칸이 가장 많은 칸 선택
            if maze[i][j] == 0:
                adjacent_cnt, vacant_cnt = get_adjacent_cnt(num, i, j)
                if adjacent_cnt > max_adjacent_cnt:
                    max_adjacent_cnt = adjacent_cnt
                    max_vacant_cnt = vacant_cnt
                    max_idx = [i, j]
                elif adjacent_cnt == max_adjacent_cnt and vacant_cnt > max_vacant_cnt:
                    max_adjacent_cnt = adjacent_cnt
                    max_vacant_cnt = vacant_cnt
                    max_idx = [i, j]
    maze[max_idx[0]][max_idx[1]] = num

# 만족도
answer = 0
for i in range(N):
    for j in range(N):
        answer += get_satisfaction(maze[i][j], i, j)

print(answer)

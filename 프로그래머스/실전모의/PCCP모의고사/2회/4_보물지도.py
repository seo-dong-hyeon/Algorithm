from collections import deque

def solution(n, m, hole):
    answer = 0
    max_size = 1001

    # 당장 점프를 해서 비용이 적더라도 후에 다른 경우가 발생할 수 있으므로
    # 해당 칸에서의 최소 비용은 
    # 점프했을 때와 안했을 때 경우를 나눠서 계산
    maze = [[[1e9 for _ in range(max_size)] for _ in range(max_size)] for _ in range(2)]
    for x, y in hole:
        maze[0][m - y + 1][x] = -1    
        maze[1][m - y + 1][x] = -1    

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    dq.append([m, 1, 0, True])
    maze[1][m][1] = 0
    while dq:
        x, y, cost, flag = dq.popleft()

        # 그냥 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1 <= nx <= m and 1 <= ny <= n and maze[flag][nx][ny] != -1:
                if maze[flag][nx][ny] > cost + 1:
                    dq.append([nx, ny, cost + 1, flag])
                    maze[flag][nx][ny] = cost + 1

        # 점프
        if flag:
            flag = False
            for i in range(4):
                nx = x + (dx[i] * 2)
                ny = y + (dy[i] * 2)
                if 1 <= nx <= m and 1 <= ny <= n and maze[flag][nx][ny] != -1:
                    if maze[flag][nx][ny] > cost + 1:
                        dq.append([nx, ny, cost + 1, flag])
                        maze[flag][nx][ny] = cost + 1

    answer = min(maze[0][1][n], maze[1][1][n])
    answer = answer if answer != 1e9 else -1

    return answer

# print(solution(4, 4, [[2, 3], [3, 3]]))
# print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))
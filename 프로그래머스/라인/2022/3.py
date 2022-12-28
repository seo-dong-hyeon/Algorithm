from typing import List
from collections import deque

def solution(wall: List[str]) -> List[List[int]]:
    n, m = len(wall), len(wall[0])
    answer = [[-1] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    dq.append([n - 1, 0, 1])
    answer[n - 1][0] = 1
    while dq:
        x, y, cost = dq.popleft()
        # 상하좌우
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and wall[nx][ny] == 'H':
                if answer[nx][ny] == -1 or answer[nx][ny] > cost + 1:
                    dq.append([nx, ny, cost + 1])
                    answer[nx][ny] = cost + 1

        # 왼쪽 한 칸 옆
        if y - 2 >= 0 and wall[x][y - 1] == '.' and wall[x][y - 2] == 'H':
            if x - 1 >= 0 and wall[x - 1][y - 2] == '.' and wall[x - 1][y - 1] == '.' and wall[x - 1][y] == '.':
                if answer[x][y - 2] == -1 or answer[x][y - 2] > cost + 1:
                    dq.append([x, y - 2, cost + 1])
                    answer[x][y - 2] = cost + 1

        # 왼쪽 두 칸 옆
        if y - 3 >= 0 and wall[x][y - 1] == '.' and wall[x][y - 2] == '.' and wall[x][y - 3] == 'H':
            if x - 1 >= 0 and wall[x - 1][y - 3] == '.' and wall[x - 1][y - 2] == '.' and wall[x - 1][y - 1] == '.' and wall[x - 1][y] == '.':
                if answer[x][y - 3] == -1 or answer[x][y - 3] > cost + 1:
                    dq.append([x, y - 3, cost + 1])
                    answer[x][y - 3] = cost + 1

        # 오른쪽 한 칸 옆
        if y + 2 < m and wall[x][y + 1] == '.' and wall[x][y + 2] == 'H':
            if x - 1 >= 0 and wall[x - 1][y] == '.' and wall[x - 1][y + 1] == '.' and wall[x - 1][y + 2] == '.':
                if answer[x][y + 2] == -1 or answer[x][y + 2] > cost + 1:
                    dq.append([x, y + 2, cost + 1])
                    answer[x][y + 2] = cost + 1

        # 오른쪽 두 칸 옆
        if y + 3 < m and wall[x][y + 1] == '.' and wall[x][y + 2] == '.' and wall[x][y + 3] == 'H':
            if x - 1 >= 0 and wall[x - 1][y] == '.' and wall[x - 1][y + 1] == '.' and wall[x - 1][y + 2] == '.' and wall[x - 1][y + 3] == '.':
                if answer[x][y + 3] == -1 or answer[x][y + 3] > cost + 1:
                    dq.append([x, y + 3, cost + 1])
                    answer[x][y + 3] = cost + 1

        # 두 칸 위
        if x - 2 >= 0 and wall[x - 2][y] == 'H' and wall[x - 1][y] == '.':
            if answer[x - 2][y] == -1 or answer[x - 2][y] > cost + 1:
                dq.append([x - 2, y, cost + 1])
                answer[x - 2][y] = cost + 1

        # 대각선 오른쪽 위
        if x - 1 >= 0 and y + 1 < m and wall[x - 1][y + 1] == 'H' and wall[x - 1][y] == '.' and wall[x][y + 1] == '.':
            if answer[x - 1][y + 1] == -1 or answer[x - 1][y + 1] > cost + 1:
                dq.append([x - 1, y + 1, cost + 1])
                answer[x - 1][y + 1] = cost + 1

        # 대각선 왼쪽 위
        if x - 1 >= 0 and y - 1 >= 0 and wall[x - 1][y - 1] == 'H' and wall[x - 1][y] == '.' and wall[x][y - 1] == '.':
            if answer[x - 1][y - 1] == -1 or answer[x - 1][y - 1] > cost + 1:
                dq.append([x - 1, y - 1, cost + 1])
                answer[x - 1][y - 1] = cost + 1

    for i in range(n):
        for j in range(m):
            if wall[i][j] != 'H': 
                answer[i][j] = 0

    return answer
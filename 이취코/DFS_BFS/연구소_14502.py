# 벽 세우기 -> 순열/조합
# 바이러스 퍼져나가기 -> bfs
import sys
from itertools import combinations
import copy
from collections import deque

def bfs(maze):
    dq = deque()
    for virus in viruses:
        dq.append(virus)

    cnt = 0
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and maze[nx][ny] == 0:
                maze[nx][ny] = 2
                dq.append([nx, ny])
                cnt += 1

    return cnt


N, M = map(int, sys.stdin.readline().rstrip().split())
maze = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empties = []
viruses = []
empty_cnt = 0
for i in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(row)):
        if row[j] == 0:
            empties.append([i, j])
            empty_cnt += 1
        elif row[j] == 2:
            viruses.append([i, j])
    maze.append(row)

answer = 0
for candidates in list(combinations(empties, 3)):
    tmp = copy.deepcopy(maze)
    for x, y in candidates:
        tmp[x][y] = 1
    answer = max(answer, empty_cnt - bfs(tmp) - 3)

print(answer)
# 벽 세우기(순열/조합) + dfs
import sys
from itertools import combinations
from copy import deepcopy

def dfs(maze):
    flag = True
    for x, y in T:
        for i in range(4):
            nx = x
            ny = y
            while True:
                nx += dx[i]
                ny += dy[i] 
                if nx < 0 or nx >= N or ny < 0 or ny >= N or maze[nx][ny] == 'O':
                    break
                if maze[nx][ny] == 'S':
                    flag = False
                    break
            if not flag:
                return flag
    return flag


maze = []
N = int(sys.stdin.readline().rstrip())
T = []
candidates = []

for i in range(N):
    rows = list(sys.stdin.readline().rstrip().split())
    maze.append(rows)
    for j in range(N):
        if rows[j] == 'X':
            candidates.append([i, j])
        elif rows[j] == 'T':
            T.append([i, j])
candidates.sort()

dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]

flag = False
for candidate in list(combinations(candidates, 3)):
    for x, y in list(candidate):
        maze[x][y] = 'O'
    flag = dfs(deepcopy(maze))
    if flag:
        break
    for x, y in list(candidate):
        maze[x][y] = 'X'

print("YES" if flag else "NO")
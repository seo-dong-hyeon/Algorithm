import sys

H, W = map(int, sys.stdin.readline().rstrip().split())
maze = [['.'] * W for _ in range(H)]
checked = [[-1] * W for _ in range(H)]

for i in range(H):
    row = sys.stdin.readline().rstrip()
    for j in range(W):
        if row[j] == 'c':
            maze[i][j] = 'c'
            checked[i][j] = 0

for x in range(H):
    for y in range(W):
        if checked[x][y] != 0:
            ny = y - 1
            time = 1
            flag = False
            while ny >= 0:
                if maze[x][ny] == 'c':
                    flag = True
                    break
                ny -= 1
                time += 1
            if flag:
                checked[x][y] = time

for x in range(H):
    for y in range(W):
        print(checked[x][y], end=' ')
    print()
print()
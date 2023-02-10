def solution(board):
    answer = 0

    n = len(board)
    bombs = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bombs.append([i, j])

    checked = [[0 for _ in range(n)] for _ in range(n)]
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    for x, y in bombs:
        checked[x][y] = 1
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                checked[nx][ny] = 1

    cnt = 0
    for i in range(n):
        for j in range(n):
            if checked[i][j] == 1:
                cnt += 1
    answer = n * n - cnt

    return answer

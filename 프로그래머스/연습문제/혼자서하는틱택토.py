def dfs(visited, depth, O_list, X_list, order):
    if depth == len(O_list) + len(X_list):
        return True

    # 가로 방향 체크
    for i in range(3):
        mark = visited[i][0]
        if mark == '.':
            continue
        equal = True
        for j in range(3):
            if visited[i][j] != mark:
                equal = False
                break
        if equal:
            return False

    # 세로 방향 체크
    for i in range(3):
        mark = visited[0][i]
        if mark == '.':
            continue
        equal = True
        for j in range(3):
            if visited[j][i] != mark:
                equal = False
                break
        if equal:
            return False

    # 대각선 방향 체크
    if visited[0][0] != '.' and visited[0][0] == visited[1][1] and visited[0][0] == visited[2][2]:
        return False
    if visited[0][2] != '.' and visited[0][2] == visited[1][1] and visited[0][2] == visited[2][0]:
        return False

    if order == 'O':
        for x, y in O_list:
            if visited[x][y] == '.':
                visited[x][y] = 'O'
                # 리턴값이 True 이면 리턴
                if dfs(visited, depth + 1, O_list, X_list, 'X'):
                    return True
                visited[x][y] = '.'
    else:
        for x, y in X_list:
            if visited[x][y] == '.':
                visited[x][y] = 'X'
                # 리턴값이 True 이면 리턴
                if dfs(visited, depth + 1, O_list, X_list, 'O'):
                    return True
                visited[x][y] = '.'

    return False


def solution(board):
    answer = -1

    O_list = []
    X_list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                O_list.append([i, j])
            elif board[i][j] == 'X':
                X_list.append([i, j])

    visited = [['.' for _ in range(3)] for _ in range(3)]

    answer = 1 if dfs(visited, 0, O_list, X_list, 'O') else 0

    return answer

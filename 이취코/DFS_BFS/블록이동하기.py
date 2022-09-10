# 구현 + BFS + 해시
# 블록 이동하기 -> 해시
# 두 공간을 한 번에 점유할 때
# 이동 조건
# 각 칸에서의 최소값이 아닌 
# 두 칸의 조합에서의 최소값 일 때 이동
# checked[x1][y1] > cnt + 1 and checked[x2][y2] > cnt + 1 X
# -> checked[(x1, y1, x2, y2)] > cnt + 1
from collections import deque

# 이동 가능 여부 체크
def check_move(N, x1, y1, x2, y2, board, checked, cnt):
    if x1 >= 0 and x1 < N and y1 >= 0 and y1 < N and x2 >= 0 and x2 < N and y2 >= 0 and y2 < N:
        if board[x1][y1] == 1 or board[x2][y2] == 1:
            return False
        # 해당 좌표의 조합으로 
        # 처음 왔거나 기존보다 효율적으로 왔을때만 이동
        pos = (x1, y1, x2, y2)
        if pos not in checked or checked[pos] > cnt + 1:
            return True
    return False


def solution(board):
    answer = 1e9

    N = len(board)
    checked = {}
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    dq.append([[0, 0], [0, 1], 0])
    while dq:
        wheel1, wheel2, cnt = dq.popleft()
        x1, y1 = wheel1
        x2, y2 = wheel2
        # 도착 시 확인
        if (x1 == N - 1 and y1 == N - 1) or (x2 == N - 1 and y2 == N - 1):
            answer = min(answer, cnt)

        # 상하좌우 이동
        for i in range(4):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]
            if check_move(N, nx1, ny1, nx2, ny2, board, checked, cnt):
                checked[(nx1, ny1, nx2, ny2)] = cnt + 1
                dq.append([[nx1, ny1], [nx2, ny2], cnt + 1])

        # 회전
        # 가로 방향
        if x1 == x2:
            if x1 - 1 >= 0:
                # 왼쪽 위로
                if board[x2 - 1][y2] == 0:
                    nx1, ny1 = x1 - 1, y1
                    nx2, ny2 = x1, y1
                    if check_move(N, nx1, ny1, nx2, ny2, board, checked, cnt):
                        checked[(nx1, ny1, nx2, ny2)] = cnt + 1
                        dq.append([[nx1, ny1], [nx2, ny2], cnt + 1])
                # 오른쪽 위로
                if board[x1 - 1][y1] == 0:
                    nx1, ny1 = x2 - 1, y2
                    nx2, ny2 = x2, y2
                    if check_move(N, nx1, ny1, nx2, ny2, board, checked, cnt):
                        checked[(nx1, ny1, nx2, ny2)] = cnt + 1
                        dq.append([[nx1, ny1], [nx2, ny2], cnt + 1])
            if x1 + 1 < N:
                # 왼쪽 아래로
                if board[x2 + 1][y2] == 0:
                    nx1, ny1 = x1, y1
                    nx2, ny2 = x1 + 1, y1
                    if check_move(N, nx1, ny1, nx2, ny2, board, checked, cnt):
                        checked[(nx1, ny1, nx2, ny2)] = cnt + 1
                        dq.append([[nx1, ny1], [nx2, ny2], cnt + 1])
                # 오른쪽 아래로
                if board[x1 + 1][y1] == 0:
                    nx1, ny1 = x2, y2
                    nx2, ny2 = x2 + 1, y2
                    if check_move(N, nx1, ny1, nx2, ny2, board, checked, cnt):
                        checked[(nx1, ny1, nx2, ny2)] = cnt + 1
                        dq.append([[nx1, ny1], [nx2, ny2], cnt + 1])
        # 세로 방향
        else:
            if y1 - 1 >= 0:
                # 왼쪽 위로
                if board[x2][y2 - 1] == 0:
                    nx1, ny1 = x1, y1 - 1
                    nx2, ny2 = x1, y1
                    if check_move(N, nx1, ny1, nx2, ny2, board, checked, cnt):
                        checked[(nx1, ny1, nx2, ny2)] = cnt + 1
                        dq.append([[nx1, ny1], [nx2, ny2], cnt + 1])
                # 왼쪽 아래로
                if board[x1][y1 - 1] == 0:
                    nx1, ny1 = x2, y2 - 1
                    nx2, ny2 = x2, y2
                    if check_move(N, nx1, ny1, nx2, ny2, board, checked, cnt):
                        checked[(nx1, ny1, nx2, ny2)] = cnt + 1
                        dq.append([[nx1, ny1], [nx2, ny2], cnt + 1])
            if y1 + 1 < N:
                # 오른쪽 위로
                if board[x2][y2 + 1] == 0:
                    nx1, ny1 = x1, y1
                    nx2, ny2 = x1, y1 + 1
                    if check_move(N, nx1, ny1, nx2, ny2, board, checked, cnt):
                        checked[(nx1, ny1, nx2, ny2)] = cnt + 1
                        dq.append([[nx1, ny1], [nx2, ny2], cnt + 1])
                # 오른쪽 아래로
                if board[x1][y1 + 1] == 0:
                    nx1, ny1 = x2, y2
                    nx2, ny2 = x2, y2 + 1
                    if check_move(N, nx1, ny1, nx2, ny2, board, checked, cnt):
                        checked[(nx1, ny1, nx2, ny2)] = cnt + 1
                        dq.append([[nx1, ny1], [nx2, ny2], cnt + 1])

    return answer

print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))
# 백트래킹 - N-Queen 문제
# 모든 행, 열에 대해 리스트 만들기 X
# 1차원 리스트 -> board[row] = col == row행 col열에 체스말 놓음
import sys

def checkValid(row, col):
    for i in range(row):
        # 일직선 검사
        if board[i] == col: 
            return False
        # 대각선 검사
        if (row - i) == abs(col - board[i]):
            return False
    return True

def dfs(row):
    if row == N:        # 마지막 칸까지 왔으면 경우의 수 추가
        global answer
        answer += 1
        return 

    for i in range(N):
        board[row] = i
        if checkValid(row, i):
            board[row] = i      # row행 col열에 체스말 놓음
            dfs(row + 1)
            board[row] = -1     # row행 col열에 체스말 뺌
    return

N = int(sys.stdin.readline().rstrip())
board = [-1] * N
answer = 0

dfs(0)

print(answer)

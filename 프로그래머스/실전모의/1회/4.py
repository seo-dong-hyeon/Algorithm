# 75 %

from copy import deepcopy

minCnt = 1e9

def check(s, t):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != t[i][j]:
                return False
    return True

def go(state, target, row, col, cnt):
    global minCnt
    if cnt > minCnt:
        return
    
    if check(state, target):
        minCnt = min(minCnt, cnt)
        return

    if row < len(state):
        go(state, target, row + 1, col, cnt) # 현재 행 안 뒤집음
        newState = deepcopy(state)
        for i in range(len(state[0])):
            if newState[row][i] == 0:
                newState[row][i] = 1
            else:
                newState[row][i] = 0
        go(newState, target, row + 1, col, cnt + 1) # 현재 행 뒤집음
    else:
        if col < len(state[0]):
            go(state, target, row, col + 1, cnt) # 현재 열 안 뒤집음
            newState = deepcopy(state)
            for i in range(len(state)):
                if newState[i][col] == 0:
                    newState[i][col] = 1
                else:
                    newState[i][col] = 0
            go(newState, target, row, col + 1, cnt + 1) # 현재 열 뒤집음


def solution(beginning, target):
    answer = 0
    go(beginning, target, 0, 0, 0)

    if minCnt == 1e9:
        answer = -1
    else:
        answer = minCnt

    return answer
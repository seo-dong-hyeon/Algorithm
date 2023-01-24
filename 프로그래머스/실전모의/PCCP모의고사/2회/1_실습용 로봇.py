def solution(command):
    answer = []

    # 상 우 하 좌
    dx = [0, 1, 0, -1]   
    dy = [1, 0, -1, 0]
    d = 0
    pos = [0, 0]
    for c in command:
        if c == 'R':
            d = (d + 1) % 4
        elif c == 'L':
            d = (d - 1) % 4
        elif c == 'G':
            pos = [pos[0] + dx[d], pos[1] + dy[d]]
        elif c == 'B':
            if d == 0:
                nd = 2
            elif d == 1:
                nd = 3
            elif d == 2:
                nd = 0
            elif d == 3:
                nd = 1
            pos = [pos[0] + dx[nd], pos[1] + dy[nd]]

    answer = pos

    return answer

import sys
from collections import deque

def check_visited(x, y, cnt, visited):
    if (x, y) not in visited or visited[(x, y)] > cnt:
        return True
    else:
        return False


answer = -1
a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
visited = {}

dq = deque()
dq.append([0, 0, 0])
visited[(0, 0)] = 0
while dq:
    x, y, cnt = dq.popleft()
    if x == c and y == d:
        answer = cnt
        break
    move_list = [[a, y], [x, b], # [F(x): Fill x]
                 [0, y], [x, 0]  # [E(x): Empty x]
                ]
    # [M(x,y): Move water from x to y)]
    nx, ny = (x - (b - y), b) if x > b - y else (0, x + y)
    move_list.append([nx, ny])
    # [M(y,x): Move water from y to x)]
    nx, ny = (a, y - (a - x)) if y > a - x else (x + y, 0)
    move_list.append([nx, ny])

    # 물통 이동
    for nx, ny in move_list:
        if check_visited(nx, ny, cnt + 1, visited):
            dq.append([nx, ny, cnt + 1])
            visited[(nx, ny)] = cnt + 1

print(answer)

import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
gears = []

for _ in range(T):
    dq = deque()
    for i in sys.stdin.readline().rstrip():
        dq.append(i)
    gears.append(dq)


left = 6
right = 2
K = int(sys.stdin.readline().rstrip())
for _ in range(K):
    directions = [0] * T
    num, d = map(int, sys.stdin.readline().rstrip().split())
    num -= 1
    directions[num] = d
    # 왼쪽 톱니바퀴들 회전 기록
    for i in range(num - 1, -1, -1):
        if gears[i][right] == gears[i + 1][left]:
            break
        directions[i] = directions[i + 1] * -1
    # 오른쪽 톱니바퀴들 회전 기록
    for i in range(num + 1, T):
        if gears[i - 1][right] == gears[i][left]:
            break
        directions[i] = directions[i - 1] * -1
    # 톱니바퀴 회전
    for i, d in enumerate(directions):
        if d == 1:
            gears[i].appendleft(gears[i].pop())
        elif d == -1:
            gears[i].append(gears[i].popleft())

answer = 0
for i in range(T):
    if gears[i][0] == '1':
        answer += 1

print(answer)


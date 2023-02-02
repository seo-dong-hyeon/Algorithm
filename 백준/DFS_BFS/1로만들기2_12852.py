import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
max_num = 1000001
cost = [1e9] * max_num
before = [0] * max_num

dq = deque()
# [현재 위치, 해당 위치까지 비용]
dq.append([N, 0])
# 각 위치별 비용
cost[N] = 0
# 이전 위치
before[N] = N
while dq:
    x, now_cost = dq.popleft()
    if x == 1:
        break
    # 더 적은 비용으로 해당 위치에 갈 수 있다면 이동
    # 해당 위치까지의 비용, 해당 위치 이전의 위치 갱신
    if x % 3 == 0:
        i = x // 3
        if 1 <= i and cost[i] > now_cost + 1:
            dq.append([i, now_cost + 1])
            cost[i] = now_cost + 1
            before[i] = x
    if x % 2 == 0:
        i = x // 2
        if 1 <= i and cost[i] > now_cost + 1:
            dq.append([i, now_cost + 1])
            cost[i] = now_cost + 1
            before[i] = x
    i = x - 1
    if 1 <= i and cost[i] > now_cost + 1:
        dq.append([i, now_cost + 1])
        cost[i] = now_cost + 1
        before[i] = x

# 재귀적으로 이전 위치 탐색
paths = []
x = 1
while x != N:
    paths.append(x)
    x = before[x]
paths.append(N)

print(cost[1])
for _path in paths[::-1]:
    print(_path, end=' ')
print()
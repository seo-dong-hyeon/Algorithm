import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
max_num = 100010
cost = [1e9] * max_num
before = [0] * max_num

dq = deque()
# [현재 위치, 해당 위치까지 비용]
dq.append([N, 0])
cost[N] = 0
# 이전 위치
before[N] = N
while dq:
    num, now_cost = dq.popleft()
    if num == K:
        break
    # 3가지 경우만 탐색
    for i in (num - 1, num + 1, num * 2):
        if 0 <= i < max_num:
            # 더 적은 비용으로 해당 위치에 갈 수 있다면 갱신
            if cost[i] > now_cost + 1:
                dq.append([i, now_cost + 1])
                cost[i] = now_cost + 1
                before[i] = num

paths = []
num = K
while num != N:
    paths.append(num)
    num = before[num]
paths.append(N)

print(cost[K])
for _path in paths[::-1]:
    print(_path, end=' ')
print()
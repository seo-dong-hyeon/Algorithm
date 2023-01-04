import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
max_num = 100010
cost = [1e9] * max_num

dq = deque()
# [현재 위치, 해당 위치까지 비용]
dq.append([N, 0])
cost[N] = 0
cnt = 0
while dq:
    num, now_cost = dq.popleft()
    # 경로에 도달했으면 방법의 수 증가
    if num == K:
        cnt += 1
        continue
    for i in (num - 1, num + 1, num * 2):
        if 0 <= i < max_num:
            # 비용이 작거나 같은 비용으로 해당 위치에 갈 수 있을 때 이동
            # 경로에 도달하는 방법의 수를 구할 땐 
            # num == K로 가는 경우가 모두 도달해야 하므로 
            # 비용이 같은 경우도 추가
            if cost[i] >= now_cost + 1:
                dq.append([i, now_cost + 1])
                cost[i] = now_cost + 1

print(cost[K])
print(cnt)
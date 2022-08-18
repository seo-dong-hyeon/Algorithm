# 위상정렬
# 방향 그래프에서 순서대로 나열
import sys
from collections import deque
import copy

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)    # 진입차수
times = [0] * (N + 1)       # 각 노드별 비용

for i in range(1, N + 1):
    info = list(map(int, sys.stdin.readline().rstrip().split()))
    times[i] = info[0]
    for j in info[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

dq = deque()    # 데큐 사용
# 진입 차수가 0 -> 시작 노드
for i in range(1, N + 1):
    if indegree[i] == 0:
        dq.append(i)

orders = []
totalTimes = copy.deepcopy(times)   # 누적시간(비용) -> 각 노드별 비용으로 초기화
while dq:
    v = dq.popleft()
    # orders.append(v)  # 노드 순서
    for nextV in graph[v]:
        # 현재 노드 누적 비용 = max(현재 노드 누적비용, 이전 노드 누적비용 + 현재 노드 비용)
        totalTimes[nextV] = max(totalTimes[nextV], totalTimes[v] + times[nextV])
        indegree[nextV] -= 1
        # 진입 차수가 0 -> 데큐에
        if indegree[nextV] == 0:
            dq.append(nextV)

for i in range(1, len(totalTimes)):
    print(totalTimes[i])
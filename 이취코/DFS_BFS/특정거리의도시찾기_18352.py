# 특정 지점부터 거리가 K인 도시 찾기
# 보통 다익스트라
# 모든 도로의 거리가 동일 -> bfs로 가능
import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().rstrip().split())

graph = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[A].append(B)

dq = deque()
dq.append(X)
distance = [-1] * (N + 1)   # 도로의 거리 기본값 = -1
distance[X] = 0

while dq:
    node = dq.popleft()
    for next_node in graph[node]:
        if distance[next_node] == -1:   # 거리가 -1 -> 아직 방문 X -> visited 리스트 필요 X
            distance[next_node] = distance[node] + 1
            dq.append(next_node)

flag = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        flag = True

if not flag:
    print(-1)
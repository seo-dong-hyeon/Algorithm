# 다익스트라
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[A].append([1, B])
    graph[B].append([1, A])

distances = [1e9] * (N + 1)

dq = deque()
dq.append([0, 1])
distances[1] = 0

while dq:
    dist, node = dq.popleft()
    if distances[node] < dist:
        continue
    distances[node] = dist
    for next_dist, next_node in graph[node]:
        cost = dist + next_dist
        if distances[next_node] > cost:
            distances[next_node] = cost
            dq.append([cost, next_node])

max_dist = max(distances[1:])
max_cnt = distances.count(max_dist)
max_idx = 0
for idx, distance in enumerate(distances[1:]):
    if max_dist == distance:
        max_idx = idx + 1
        break
    
print(max_idx, max_dist, max_cnt)
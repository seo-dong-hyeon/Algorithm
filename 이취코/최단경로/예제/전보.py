# 다익스트라
import sys
import heapq

N, M, C = map(int, sys.stdin.readline().rstrip().split())

# 간선 초기화
graph = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    X, Y, Z = map(int, sys.stdin.readline().rstrip().split())
    graph[X].append([Z, Y]) # [거리, 노드] 순서

# 거리 초기화    
distances = [1e9] * (N + 1)

# 다익스트라 알고리즘
hq = []
distances[C] = 0
heapq.heappush(hq, [0, C])
while hq:
    dist, node = heapq.heappop(hq)
    if distances[node] < dist:
        continue
    distances[node] = dist
    for next_dist, next_dest in graph[node]:
        cost = dist + next_dist
        if distances[next_dest] > cost:
            distances[next_dest] = cost
            heapq.heappush(hq, [cost, next_dest])

cnt = 0
time = 0
for distance in distances:
    if distance == 1e9:
        continue
    cnt += 1
    time = max(time, distance)

print(cnt - 1, time)

import sys
import heapq

N, M, K, X = map(int, sys.stdin.readline().rstrip().split())
graph = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[A].append([1, B])

distance = [1e9] * (N + 1)
distance[X] = 0

heap = []
heapq.heappush(heap, [0, X])
while heap:
    dist, node = heapq.heappop(heap)
    if distance[node] > dist:
        distance[node] = dist
        continue
    distance[node] = dist
    for next_dist, next_node in graph[node]:
        cost = dist + next_dist
        if distance[next_node] > cost:
            distance[next_node] = cost
            heapq.heappush(heap, [cost, next_node])

answer = []
for i in range(1, len(distance)):
    if distance[i] == K:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for i in range(len(answer)):
        print(answer[i])
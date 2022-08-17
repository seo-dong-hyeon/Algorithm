# 플로이드 와샬
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

# 간선 초기화
graph = [[1e9] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

# 연결된 노드들
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1
X, K = map(int, sys.stdin.readline().rstrip().split())

# 플로이드 와샬 알고리즘
for k in range(N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            # graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

dist = graph[1][K] + graph[K][X]
if dist > 1e9:
    dist = -1

print(dist)
# 최소 신장 트리
# 크루스칼 알고리즘
# 모든 노드들간에는 연결된 경로가 존재
# 전체 경로의 비용은 최소화
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

N, M = map(int, sys.stdin.readline().rstrip().split())
parent = [0] * (N + 1)
edges = []

for i in range(len(parent)):
    parent[i] = i

# 비용을 기준으로 정렬
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    edges.append([C, A, B])
edges.sort()

totalCost = 0
maxCost = 0
for edge in edges:
    C, A, B = edge
    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        totalCost += C
        maxCost = max(maxCost, C) # 정렬되어 있으므로 maxCost = C

print(totalCost - maxCost)

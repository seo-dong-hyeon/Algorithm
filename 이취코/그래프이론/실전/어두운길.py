# 최소 신장 트리 - 크루스칼 알고리즘
# 임의의 두 노드간에 왔다갔다 할 수 있어야
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
edges = []

totalCost = 0
for _ in range(M):
    X, Y, Z = map(int, sys.stdin.readline().rstrip().split())
    edges.append([Z, X, Y])
    totalCost += Z

parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

edges.sort()
for edge in edges:
    Z, X, Y = edge
    if find_parent(parent, X) != find_parent(parent, Y):
        union_parent(parent, X, Y)
        totalCost -= Z

print(totalCost)
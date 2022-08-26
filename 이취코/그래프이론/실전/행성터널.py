# 최소 신장 트리 - 크루스칼 알고리즘
# 여러 좌표값 중 최소값으로 연결
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

N = int(sys.stdin.readline().rstrip())

parent = [0] * (N + 1)
for i in range(N + 1):
    parent[i] = i

# 각 노드의 좌표마다 [좌표값, 노드 번호] 저장 후 좌표값 기준 정렬
xPos = []
yPos = []
zPos = []
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    xPos.append([x, i])
    yPos.append([y, i])
    zPos.append([z, i])
xPos.sort()
yPos.sort()
zPos.sort()

# 간선 정보에 각 좌표마다 인접한 좌표의 [거리 비용, 노드1, 노드2] 저장
edges = []
for i in range(N - 1):
    edges.append([xPos[i + 1][0] - xPos[i][0], xPos[i][1], xPos[i + 1][1]])
    edges.append([yPos[i + 1][0] - yPos[i][0], yPos[i][1], yPos[i + 1][1]])
    edges.append([zPos[i + 1][0] - zPos[i][0], zPos[i][1], zPos[i + 1][1]])
edges.sort()

# 크루스칼 알고리즘
answer = 0
for edge in edges:
    dist, a, b = edge
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        union_parent(parent, a, b)
        answer += dist

print(answer)
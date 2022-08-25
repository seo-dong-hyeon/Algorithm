# 여행 경로 문제
# 특정 경로 순서로 이동 가능한지 여부
# 왔던 길 되돌아 가기 가능
# 같은 집합에 속하기만 하면 가능 -> 서로소 집합
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
graph = [[1e9] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    for j, connected in enumerate(list(map(int, sys.stdin.readline().rstrip().split()))):
        graph[i][j] = connected

paths = list(map(int, sys.stdin.readline().rstrip().split()))

parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

for i in range(N + 1):
    for j in range(N + 1):
        if graph[i][j] == 1:
            union_parent(parent, i, j)

answer = "YES"
first = ""
for i, path in enumerate(paths):
    if i == 0:
        first = parent[path - 1]    # 인덱스 유의(그래프 상에서 번호 != 주어진 여행 경로)
        continue
    if parent[path - 1] != first:
        answer = "NO"
        break

print(answer)



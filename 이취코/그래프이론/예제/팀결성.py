# 서로소 집합
# 팀 결성, 같은 팀인지 확인
import sys

# 특정 원소의 부모(집합) 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

N, M = map(int, sys.stdin.readline().rstrip().split())

# 부모를 자신으로 초기화
parent = [0] * (N + 1)
for i in range(len(parent)):
    parent[i] = i
    
for _ in range(M):
    command, a, b, = map(int, sys.stdin.readline().rstrip().split())
    if command == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
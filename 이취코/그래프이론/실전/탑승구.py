# 도킹 문제(비행기 별로 도킹가능한 탑승구들이 주어질 때, 최대로 많은 비행기 도킹)
# 서로소 집합 문제
'''
1.0번 탑승구를 그림
2.각 비행기 -> 도킹가능한 가장 큰 탑승구 입장
3.해당 탑승구의 find_parent -> 루트 부모가 0번이면 더 이상 도킹 불가
4.루트 부모가 0번이 아니면 해당 탑승구 탑승
5.해당 탑승구의 왼쪽 탑승구와 union_parent
해당 과정 반복
'''
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


g = int(sys.stdin.readline().rstrip())
p = int(sys.stdin.readline().rstrip())

parent = [0] * (g + 1)
for i in range(1, g + 1):
    parent[i] = i


airplanes = []
for _ in range(p):
    airplanes.append(int(sys.stdin.readline().rstrip()))

answer = 0
for airplane in airplanes:
    num = find_parent(parent, airplane)
    if num == 0:
        break
    union_parent(parent, num, num - 1)
    answer += 1

print(answer)
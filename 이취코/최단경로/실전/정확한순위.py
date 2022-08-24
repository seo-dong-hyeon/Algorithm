# 정확한 순위를 알 수 있는 노드
# 플로이드 와샬 -> 모든 노드간의 최단 경로 파악
# 한 노드씩 루프를 돌면서 다른 노드들과 모두 연결만 되어있다면
# 정확한 순위 파악 가능
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[1e9] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j :
            graph[i][j] = 0

for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph[A][B] = 1

# 플로이드 와샬    
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(1, N + 1):   # 모든 노드를 돌면서
    flag = True
    cnt = 0
    for j in range(1, N + 1):   # 각 노드를 기준으로 다른 노드들과 연결이 되어있는지 확인
        # 한 노드라도 양방향 길이 없다면 순위 알 수 없음
        if graph[i][j] == 1e9 and graph[j][i] == 1e9:
            flag = False
            break
    if flag:
        answer += 1

print(answer)

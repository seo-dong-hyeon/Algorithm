# 다익스트라 -> 2차원 배열
import sys
import heapq

T = int(sys.stdin.readline().rstrip())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for test_case in range(T):
    N = int(sys.stdin.readline().rstrip())
    # 노드 초기화
    # graph[x][y] -> (x, y) 좌표를 노드로 보고 해당 노드에 대한 진입 비용
    graph = [[0] * N for _ in range(N)]
    for i in range(N):
        row = list(map(int, sys.stdin.readline().rstrip().split()))
        for j in range(N):
            graph[i][j] = row[j]
    
    # 거리 초기화    
    # distances[x][y] -> (x, y) 좌표를 노드로 보고 해당 노드에 대한 거리
    distances = [[1e9] * (N + 1) for _ in range(N + 1)]

    # 다익스트라 알고리즘
    hq = []
    distances[0][0] = graph[0][0]   # 초기값 -> (0, 0) 좌표의 노드
    heapq.heappush(hq, [graph[0][0], 0, 0]) # (0, 0) 좌표 노드의 진입 비용과 (0, 0) 좌표 추가
    while hq:
        dist, x, y = heapq.heappop(hq)
        if distances[x][y] < dist:
            continue
        for i in range(4):  # 상하좌우로 이동하면서
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                cost = dist + graph[nx][ny]
                # (0, 0)에서 (nx, ny) 좌표의 노드의 거리보다
                # (x, y)를 거쳐서 (nx, ny)로 가는 것이 더 가깝다면 갱신
                if distances[nx][ny] > cost:
                    distances[nx][ny] = cost
                    heapq.heappush(hq, [cost, nx, ny])

    print(distances[N - 1][N - 1])

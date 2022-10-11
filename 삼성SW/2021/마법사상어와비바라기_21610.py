from collections import deque

def move_cloud(N, x, y, di, si):
    # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    x = (x + (dx[di - 1] * si)) % N
    y = (y + (dy[di - 1] * si)) % N

    return [x, y]

N, M = map(int, input().split())
A = [[0] * N for _ in range(N)]
d = []
s = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        A[i][j] = row[j]

for i in range(M):
    di, si = map(int, input().split())
    d.append(di)
    s.append(si)

# 초기 구름
dq = deque()
dq.append([N - 1, 0])
dq.append([N - 1, 1])
dq.append([N - 2, 0])
dq.append([N - 2, 1])

for i in range(M):
    di, si = d[i], s[i]

    # 1.구름 이동
    for j in range(len(dq)):
        dq[j] = move_cloud(N, dq[j][0], dq[j][1], di, si)

    # 2.비 내림
    for j in range(len(dq)):
        x, y = dq[j]
        A[x][y] += 1

    # 3.대각선 확인 후 물 증가
    # ↖, ↗, ↘, ↙
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, 1, -1]
    cloud = [[False] * N for _ in range(N)]
    while dq:
        x, y = dq.popleft()
        cloud[x][y] = True
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > 0:
                A[x][y] += 1

    # 4.구름 제외하고 물 2이상인 칸 구름으로
    for r in range(N):
        for c in range(N):
            if A[r][c] >= 2 and cloud[r][c] is False:
                dq.append([r, c])
                A[r][c] -= 2

answer = 0
for i in range(N):
    for j in range(N):
        answer += A[i][j]

print(answer)

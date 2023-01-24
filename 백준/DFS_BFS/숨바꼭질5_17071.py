import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
max_num = 500001
# 재방문 가능
# 재방문한 곳은 짝수/홀수 시간마다 재방문(-1/+1)하므로
# 짝수 시간과 홀수 시간대로 나눠서 계산
# visited[n][0] : 짝수 시간에 위치 n을 방문한 최소시간
# visited[n][1] : 홀수 시간에 위치 n을 방문한 최소시간
visited = [[-1 for _ in range(max_num + 1)] for _ in range(2)]

dq = deque()
dq.append([N, 0])
visited[0][N] = 0
while dq:
    num, time = dq.popleft()
    # flag : time이 홀짝인지 결정
    flag = time % 2

    for i in (num - 1, num + 1, num * 2):
        if 0 <= i <= max_num:
            if visited[1 - flag][i] == -1:
                # i 위치에는 time + 1 시간에 방문 -> 홀짝을 바꿔줌
                visited[1 - flag][i] = time + 1
                dq.append((i, time + 1))

# 해당 위치에 방문할 수 있는지 확인하기.
time = 0
flag = 0
answer = -1
while K < max_num:
    if visited[flag][K] != -1:
        if visited[flag][K] <= time:
            answer = time
            break
    flag = 1 - flag
    time += 1
    K += time
    
print(answer)

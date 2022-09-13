# 파라메트릭 서치(최적화 문제 -> 결정 문제)
# 이분 탐색 문제
# 탐색의 기준인 mid 정의
# mid를 기준으로 탐색을 하되
# 해당 mid에서 특정 조건으로 계산식
# ex) 특정 높이를 넘어가는 떡 길이, 해당 집이 mid 이상으로 떨어져 있어 공유기 설치가 되는지
# 계산식의 결과가 특정 조건을 만족했는지 확인
import sys

N, C = map(int, sys.stdin.readline().rstrip().split())

x = []
for _ in range(N):
    x.append(int(sys.stdin.readline().rstrip()))
x.sort()

left = 1                # 최소 거리 차
right = x[-1] - x[0]    # 최대 거리 차
answer = 0
while left <= right:
    # mid = 가장 인접한 두 공유기의 거리 차
    # mid = 특정 좌표값이 아닌 거리차이 -> 해당 거리차이에서 주어진 조건이 만족되는지 확인
    mid = (left + right) // 2
    last_installed = x[0]       # 마지막으로 설치된 집 위치(기본값=첫번째 집)
    cnt = 1                     # 공유기 설치 수
    # mid를 기준으로 조건식
    # 두번째 집부터 순서대로 탐색
    # 탐색하는 집이 마지막으로 설치된 집에서 mid만큼 떨어진 곳이면
    # 해당 집에 공유기 설치
    for i in range(1, N):
        if x[i] >= last_installed + mid:
            last_installed = x[i]
            cnt += 1
    
    # 계산식의 결과가 특정 조건을 만족했는지 확인
    if cnt >= C:
        left = mid + 1
        answer = mid        # 최적화 문제 -> 가장 마지막에 성공한 것이 정답
    else:
        right = mid - 1

print(answer)

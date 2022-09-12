# 매 분기마다 갱신되는 값들 중 
# 최소/최대를 찾거나 정렬하는 문제
# -> 힙 or 우선순위 큐
import sys
import heapq

N = int(sys.stdin.readline().rstrip())
heap = []
answer = 0
plus = 0
for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline().rstrip()))

# 카드 묶음이 하나가 될 때까지
# 계속해서 가장 작은 두 개의 카드 묶음을 더하는 문제
while len(heap) != 1:
    # 매 분기마다 가장 작은 두 개의 카드 묶음 선택
    small1 = heapq.heappop(heap)
    small2 = heapq.heappop(heap)
    small_sum = small1 + small2
    answer += small_sum
    # 새로운 카드 묶음 저장
    heapq.heappush(heap, small_sum)

print(answer)